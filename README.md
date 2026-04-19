# evm-contract-differ

Diff deployed EVM contract bytecode, detect proxy patterns, and watch for implementation upgrades in real-time.

Useful for security researchers and protocol teams who need to verify contract integrity after upgrades or detect unauthorized changes.

## Features

- **Bytecode Diff** — Compare two deployed contracts at the bytecode level, showing changed segments with offsets
- **Proxy Detection** — Identify EIP-1967 (transparent/beacon) and EIP-1167 (minimal) proxy patterns, resolve implementation addresses
- **Upgrade Watcher** — Poll proxy contracts for implementation changes with webhook alerts
- **Opcode Disassembly** — Full EVM opcode table with disassembler for bytecode analysis

## Install

```bash
git clone https://github.com/jmpark-eng36/evm-contract-differ.git
cd evm-contract-differ
npm install
```

## Usage

### Compare two contracts

```bash
node src/index.js diff 0xContractA 0xContractB --rpc https://eth.llamarpc.com
```

### Detect proxy pattern

```bash
node src/index.js proxy 0xProxyAddress --rpc https://eth.llamarpc.com
```

Output:
```
Proxy Detection
══════════════════════════════════

  Address: 0xProxy...
  Code size: 45 bytes

  Type: EIP-1967 Transparent
  Implementation: 0xImpl...
  Impl size: 15432 bytes
  Admin: 0xAdmin...
```

### Watch for upgrades

```bash
node src/index.js watch 0xProxyAddress --rpc https://eth.llamarpc.com --interval 300
```

## Supported Proxy Patterns

- EIP-1967 Transparent Proxy (OpenZeppelin)
- EIP-1967 Beacon Proxy
- EIP-1167 Minimal Proxy (clones)
- UUPS (EIP-1822) — added recently

## Roadmap

- [ ] Diamond proxy (EIP-2535) support
- [ ] Storage layout diffing
- [ ] Verified source comparison via Etherscan API
- [ ] Historical upgrade timeline

## License

MIT
