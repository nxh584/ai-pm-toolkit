const OWNER = 'nxh584';
const REPO = 'ai-pm-toolkit';
const BRANCH = 'main';

const RAW_BASE = `https://raw.githubusercontent.com/${OWNER}/${REPO}/${BRANCH}`;
const API_BASE = `https://api.github.com/repos/${OWNER}/${REPO}/contents`;

function buildHeaders() {
  const headers = {
    'User-Agent': 'ai-pm-toolkit-cli',
    Accept: 'application/vnd.github+json'
  };

  if (process.env.GITHUB_TOKEN) {
    headers.Authorization = `Bearer ${process.env.GITHUB_TOKEN}`;
  }

  return headers;
}

function normalisePath(inputPath) {
  if (!inputPath || typeof inputPath !== 'string') {
    throw new Error('Path is required and must be a string.');
  }

  const trimmed = inputPath.trim().replace(/^\/+/, '');
  if (!trimmed) {
    throw new Error('Path cannot be empty.');
  }

  return trimmed.endsWith('.md') ? trimmed : `${trimmed}.md`;
}

function ensureDirectoryPath(inputPath) {
  if (!inputPath || typeof inputPath !== 'string') {
    throw new Error('Directory path is required and must be a string.');
  }

  return inputPath.trim().replace(/^\/+/, '').replace(/\/+$/, '');
}

async function parseResponse(response, context) {
  const contentType = response.headers.get('content-type') || '';
  const isJson = contentType.includes('application/json');
  const payload = isJson ? await response.json().catch(() => ({})) : await response.text();

  if (response.ok) {
    return payload;
  }

  if (
    response.status === 403 &&
    (response.headers.get('x-ratelimit-remaining') === '0' ||
      (typeof payload === 'object' && payload?.message?.toLowerCase().includes('rate limit')))
  ) {
    throw new Error(
      [
        'GitHub API rate limit reached for unauthenticated requests.',
        'Set a token and try again:',
        '  export GITHUB_TOKEN=your_token_here',
        `Then rerun your command (${context}).`
      ].join('\n')
    );
  }

  const detail =
    typeof payload === 'object' && payload?.message
      ? payload.message
      : typeof payload === 'string' && payload
        ? payload
        : `HTTP ${response.status}`;

  throw new Error(`Unable to ${context}. ${detail}`);
}

export async function fetchFile(path) {
  const normalised = normalisePath(path);
  const url = `${RAW_BASE}/${normalised}`;

  let response;
  try {
    response = await fetch(url, { headers: buildHeaders() });
  } catch (error) {
    throw new Error(
      `Network error while fetching file \`${normalised}\`. Check your internet connection and retry.`
    );
  }

  const payload = await parseResponse(response, `fetch file \`${normalised}\``);
  if (typeof payload !== 'string') {
    throw new Error(`Unexpected response while fetching \`${normalised}\`.`);
  }

  return {
    path: normalised,
    content: payload
  };
}

export async function fetchDirectory(path) {
  const dir = ensureDirectoryPath(path);
  const url = `${API_BASE}/${dir}?ref=${BRANCH}`;

  let response;
  try {
    response = await fetch(url, { headers: buildHeaders() });
  } catch (error) {
    throw new Error(
      `Network error while fetching directory \`${dir}\`. Check your internet connection and retry.`
    );
  }

  const payload = await parseResponse(response, `fetch directory \`${dir}\``);
  if (!Array.isArray(payload)) {
    throw new Error(`Unexpected response while reading directory \`${dir}\`.`);
  }

  return payload.map((entry) => ({
    name: entry.name,
    path: entry.path,
    type: entry.type
  }));
}

export async function fetchMarkdownDescription(path, section = 'generic') {
  const { content } = await fetchFile(path);
  const lines = content.split(/\r?\n/);

  const headingBySection = {
    prompts: 'When to use this',
    workflows: 'What this is',
    skills: 'What this skill does',
    commands: null,
    templates: null,
    generic: null
  };

  const primaryHeading = headingBySection[section] ?? null;

  function extractSection(targetHeading) {
    if (!targetHeading) {
      return '';
    }

    const headingRegex = /^##\s+(.+?)\s*$/;
    let inTarget = false;
    const collected = [];

    for (const raw of lines) {
      const line = raw.trimEnd();
      const match = line.match(headingRegex);
      if (match) {
        const heading = match[1].trim().toLowerCase();
        if (inTarget) {
          break;
        }
        if (heading === targetHeading.toLowerCase()) {
          inTarget = true;
          continue;
        }
      }

      if (inTarget) {
        collected.push(line);
      }
    }

    return collected.join('\n').trim();
  }

  function firstMeaningfulParagraph() {
    const bucket = [];
    let inCodeBlock = false;

    for (const raw of lines) {
      const line = raw.trim();

      if (line.startsWith('```')) {
        inCodeBlock = !inCodeBlock;
        continue;
      }
      if (inCodeBlock) {
        continue;
      }

      if (!line) {
        if (bucket.length) {
          break;
        }
        continue;
      }

      if (line.startsWith('#') || line.startsWith('|') || line.startsWith('>')) {
        continue;
      }

      if (/^(-|\*)\s+/.test(line) || /^\d+\.\s+/.test(line)) {
        if (bucket.length) {
          break;
        }
        continue;
      }

      bucket.push(line);
      if (bucket.length >= 2) {
        break;
      }
    }

    return bucket.join(' ').trim();
  }

  let description = '';
  if (primaryHeading) {
    description = extractSection(primaryHeading);

    if (!description && section === 'skills') {
      description = extractSection('When to load this skill');
    }
  }

  if (!description) {
    description = firstMeaningfulParagraph();
  }

  const flattened = description.replace(/\s+/g, ' ').trim();
  return flattened || 'No description available.';
}

export const REPO_META = {
  owner: OWNER,
  repo: REPO,
  branch: BRANCH,
  rawBase: RAW_BASE,
  apiBase: API_BASE
};
