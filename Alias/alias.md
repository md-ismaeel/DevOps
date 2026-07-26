# Terminal Alias

Create a custom terminal command named `....`.

## Table of Contents

- [Introduction](#-introduction)
- [Prerequisites](#-prerequisites)
- [Check Your Shell](#-check-your-shell)
- [Setup the Alias](#-setup-the-alias)
- [Reload the Shell Configuration](#-reload-the-shell-configuration)
- [Verify the Alias](#-verify-the-alias)
- [Usage](#-usage)
- [Troubleshooting](#-troubleshooting)
- [Remove the Alias](#-remove-the-alias)

## Prerequisites

Before you begin, make sure you have:

- Linux, macOS, or WSL
- Bash or Zsh shell
- A terminal application

## Check Your Shell

Run the following command:

```bash
echo $SHELL
```

### Example Output

For **Bash**

```text
/bin/bash
```

For **Zsh**

```text
/bin/zsh
```

## ⚙️ Setup the Alias

### For Zsh Users

Open the Zsh configuration file:

```bash
nano ~/.zshrc
```

Add the following line at the end of the file:

```bash
alias clr='clear'
```

Save and exit.

Reload the configuration:

```bash
source ~/.zshrc
```

### For Bash Users

Open the Bash configuration file:

```bash
nano ~/.bashrc
```

Add:

```bash
alias clr='clear'
```

Save and exit.

Reload the configuration:

```bash
source ~/.bashrc
```

## Verify the Alias

Run:

```bash
alias clr
```

If you see the above output, the alias has been created successfully.

## Usage

Simply type:

```bash
clr
```

The terminal screen will be cleared.

## Troubleshooting

### `clr: command not found`

Reload your shell configuration:

**Zsh**

```bash
source ~/.zshrc
```

**Bash**

```bash
source ~/.bashrc
```

Check whether the alias exists:

```bash
alias
```

Look for:

```text
clr='clear'
```

## Remove the Alias

### Temporary (Current Session Only)

```bash
unalias clr
```

### Permanent

Open your shell configuration file.

**Zsh**

```bash
nano ~/.zshrc
```

**Bash**

```bash
nano ~/.bashrc
```

Delete this line:

```bash
alias clr='clear'
```

Reload the configuration:

```bash
source ~/.zshrc
```

or

```bash
source ~/.bashrc
```

## Quick Reference

| Task                | Command             |
| ------------------- | ------------------- |
| Check current shell | `echo $SHELL`       |
| Edit Zsh config     | `nano ~/.zshrc`     |
| Edit Bash config    | `nano ~/.bashrc`    |
| Add alias           | `alias clr='clear'` |
| Reload Zsh          | `source ~/.zshrc`   |
| Reload Bash         | `source ~/.bashrc`  |
| Verify alias        | `alias clr`         |
| Use alias           | `clr`               |
| Remove alias        | `unalias clr`       |


