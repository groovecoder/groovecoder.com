---
layout: post
title: Slopsquatting - When AI Hallucinates Package Names
date: '2026-01-24 10:00:00 -0600'
tags:
- security
- ai
- supply-chain
- npm
---

I built a proof-of-concept [slopsquatting](https://en.wikipedia.org/wiki/Slopsquatting) attack.

## What is Slopsquatting?

AI coding assistants sometimes hallucinate package names. They suggest packages that don't exist. Developers install these fake suggestions.

Attackers can register these hallucinated names first. Then they wait.

## The Attack Chain

1. An LLM suggests a package that doesn't exist
2. A developer runs `npm install` without checking
3. The attacker's package runs on the developer's machine
4. Game over

## My Proof of Concept

I registered `arangoql` on npm. The name combines ArangoDB and GraphQL. It sounds real. An LLM might suggest it.

The package is harmless. It only shows a warning. But real attacks could:

- Steal environment variables
- Exfiltrate source code
- Install backdoors
- Modify files

## Why Track This?

I want data. How often do people install hallucinated packages? The package logs when someone installs it. Nothing personal. Just counts.

This helps us understand the risk.

## Protect Yourself

- Check package names on npm before installing
- Read the package.json postinstall scripts
- Look at download counts and maintainers
- Use lock files
- Run `npm audit`
- Don't trust AI suggestions blindly

## The Code

GitHub: [github.com/groovecoder/arangoql](https://github.com/groovecoder/arangoql)
NPM: [npmjs.com/package/arangoql](https://www.npmjs.com/package/arangoql)

If you installed this package, you proved the attack works. Thanks for the data point.
