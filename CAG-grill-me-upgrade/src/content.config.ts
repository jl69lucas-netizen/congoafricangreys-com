import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const birds = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/birds' }),
  schema: z.object({
    name: z.string(),
    variant: z.enum(['congo', 'timneh']),
    sex: z.enum(['male', 'female', 'unknown']),
    hatchYear: z.number(),
    price: z.number(),
    status: z.enum(['available', 'reserved', 'sold']),
    personality: z.string(),
    traits: z.array(z.string()),
    image: z.string().optional(),
  }),
});

const careGuides = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/care-guides' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    category: z.enum(['diet', 'enrichment', 'health', 'training', 'housing']),
    publishedAt: z.date(),
    featured: z.boolean().default(false),
  }),
});

export const collections = { birds, 'care-guides': careGuides };
