#!/usr/bin/env node

import chalk from 'chalk';
import { Command } from 'commander';

import { runCopy } from '../lib/commands/copy.js';
import { runGet } from '../lib/commands/get.js';
import { runList } from '../lib/commands/list.js';
import { runSearch } from '../lib/commands/search.js';

const program = new Command();

program
  .name('ai-pm-toolkit')
  .description('Discover and use AI PM Toolkit prompts, skills, workflows, and commands from your terminal.')
  .version('1.0.0');

program
  .command('list')
  .description('List toolkit resources by section.')
  .argument('[section]', 'Section to list: prompts, skills, workflows, templates, commands, all')
  .action(async (section) => {
    await runList(section);
  });

program
  .command('get')
  .description('Fetch and print a toolkit file by path.')
  .argument('<path>', 'Path such as prompts/problem-shaping/clarify-ambiguity')
  .action(async (path) => {
    await runGet(path);
  });

program
  .command('search')
  .description('Search toolkit content by filename and description.')
  .argument('<query>', 'Search query')
  .action(async (query) => {
    await runSearch(query);
  });

program
  .command('copy')
  .description('Fetch a toolkit file and copy its contents to clipboard.')
  .argument('<path>', 'Path such as prompts/problem-shaping/clarify-ambiguity')
  .action(async (path) => {
    await runCopy(path);
  });

program.configureOutput({
  outputError: (str, write) => write(chalk.red(str))
});

try {
  await program.parseAsync(process.argv);
} catch (error) {
  const message = error instanceof Error ? error.message : 'Unexpected CLI error.';
  console.error(chalk.red(`Error: ${message}`));
  process.exit(1);
}
