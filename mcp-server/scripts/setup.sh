#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MCP_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

print_error() {
  printf "Error: %s\n" "$1" >&2
}

print_info() {
  printf "%s\n" "$1"
}

require_python() {
  if ! command -v python3 >/dev/null 2>&1; then
    print_error "python3 was not found. Install Python 3.10+ and rerun this script."
    exit 1
  fi

  local version
  version="$(python3 --version 2>&1 | awk '{print $2}')"

  if ! python3 - <<'PY'
import sys
raise SystemExit(0 if sys.version_info >= (3, 10) else 1)
PY
  then
    print_error "Python ${version} detected. Python 3.10+ is required."
    exit 1
  fi

  print_info "Python ${version} detected."
}

install_server() {
  cd "${MCP_ROOT}"

  if command -v uv >/dev/null 2>&1; then
    print_info "Detected uv. Installing with: uv pip install -e ."
    uv pip install -e .
  else
    print_info "uv not found. Installing with: pip install -e ."
    python3 -m pip install -e .
  fi
}

verify_install() {
  if command -v ai-pm-toolkit-mcp >/dev/null 2>&1; then
    print_info "Install verified: ai-pm-toolkit-mcp is available on PATH."
    return
  fi

  print_error "Install completed but ai-pm-toolkit-mcp is not on PATH."
  print_error "If you installed into a virtual environment, use that binary path in your MCP config."
  exit 1
}

print_config() {
  local os_name
  os_name="$(uname -s)"

  local config_path
  case "${os_name}" in
    Darwin)
      config_path="$HOME/.claude/claude_desktop_config.json"
      ;;
    Linux)
      config_path="$HOME/.claude/claude_desktop_config.json"
      ;;
    CYGWIN*|MINGW*|MSYS*)
      config_path='%APPDATA%\\Claude\\claude_desktop_config.json'
      ;;
    *)
      config_path="$HOME/.claude/claude_desktop_config.json"
      ;;
  esac

  print_info ""
  print_info "Claude Code MCP config file: ${config_path}"
  print_info "Use this JSON snippet:"
  cat <<'JSON'
{
  "mcpServers": {
    "ai-pm-toolkit": {
      "command": "ai-pm-toolkit-mcp"
    }
  }
}
JSON

  local venv_bin
  venv_bin="${MCP_ROOT}/.venv/bin/ai-pm-toolkit-mcp"
  print_info ""
  print_info "If using a virtual environment not on PATH, use this command path instead:"
  printf '{\n  "mcpServers": {\n    "ai-pm-toolkit": {\n      "command": "%s"\n    }\n  }\n}\n' "${venv_bin}"
}

print_next_steps() {
  print_info ""
  print_info "Next steps:"
  print_info "1. Paste the JSON into your Claude Code MCP config file."
  print_info "2. Save the file and restart Claude Code."
  print_info "3. In Claude Code, confirm the ai-pm-toolkit server appears and call list_toolkit."
}

main() {
  require_python
  install_server
  verify_install
  print_config
  print_next_steps
}

main "$@"
