import type { Page } from '@playwright/test';

export type Family = 'IMG' | 'LAYOUT' | 'NAV' | 'CSS' | 'SEM' | 'SCHEMA' | 'DUP';
export type Severity = 'blocking' | 'advisory';

export interface Defect {
  checkId: string;
  family: Family;
  viewport: number;
  message: string;
}

export interface CheckResult {
  /**
   * The number of units this check's own pass/fail predicate was evaluated
   * AGAINST. Not the number of nodes in the document, and not the number of
   * nodes it could have looked at.
   *
   * This distinction is the whole guard. A check that returns
   * `querySelectorAll('*').length` reports ~1,100 "examined" on a page where
   * it evaluated exactly one expression — so if that one expression is wrong,
   * the check reports clean forever and every zero-examined guard downstream
   * still passes. Measured on the congo-pair page: the first draft of
   * `layout-no-horizontal-overflow` reported examined=1116 having box-tested 0
   * elements. Count what you actually judged.
   */
  examined: number;
  defects: Defect[];
}

export interface Check {
  id: string;
  family: Family;
  severity: Severity;
  /** One-line statement of what a defect means, printed in reports. */
  describe: string;
  /**
   * Floor for `examined` on this check's fixtures. The meta gate asserts it.
   * Set it to the number of units the fixture genuinely contains, so a check
   * cannot pass the gate by inflating its own count.
   */
  minExamined: number;
  run(page: Page, viewport: number): Promise<CheckResult>;
}

export const registry: Check[] = [];

export function register(check: Check): void {
  if (registry.some((c) => c.id === check.id)) {
    throw new Error(`duplicate check id: ${check.id}`);
  }
  registry.push(check);
}
