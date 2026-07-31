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
  /** How many nodes/items this check actually inspected. Zero on a fixture is a FAIL. */
  examined: number;
  defects: Defect[];
}

export interface Check {
  id: string;
  family: Family;
  severity: Severity;
  /** One-line statement of what a defect means, printed in reports. */
  describe: string;
  run(page: Page, viewport: number): Promise<CheckResult>;
}

export const registry: Check[] = [];

export function register(check: Check): void {
  if (registry.some((c) => c.id === check.id)) {
    throw new Error(`duplicate check id: ${check.id}`);
  }
  registry.push(check);
}
