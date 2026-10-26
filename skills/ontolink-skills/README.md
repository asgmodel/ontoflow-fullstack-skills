# OntoLink External Skill Loader

This directory contains instructions for requesting and loading the original **external `ontolink-skills` skill**. Its coordinator, ontology and lifecycle phase packages remain in the independent official installation.

## Official source

[asgmodel/ontolink-skills](https://github.com/asgmodel/ontolink-skills)

The source command supplied by the project owner is:

```sh
npx skills add https://github.com/asgmodel/ontolink-skills --skill ontolink-skills
```

Use the global scope when the installation should be shared across projects:

```sh
npx skills add https://github.com/asgmodel/ontolink-skills --skill ontolink-skills --global --yes
```

## Start-of-session procedure

1. **Request the original skill.** Resolve `ontolink-skills` by its exact declared name through the host's skill registry. Treat the targeted dependency refresh as part of the user's authorized workflow; avoid repeated routine confirmation.
2. **Install or refresh that dependency alone.** Use the host's skill manager or the global Skills CLI command above. Select the actual host with `--agent` when appropriate. Keep the installation outside this loader directory and the application repository.
3. **Read the current instructions.** After a successful refresh, resolve the installation again and read its current `SKILL.md`, required contracts and selected phase. Load the updated source rather than relying on an earlier session's instruction snapshot.
4. **Use the existing project state.** Set `ONTOLINK_SKILL_ROOT` to the resolved package or pass `--coordinator-root`. Execute the external version's bootstrap, context and record operations according to its current instructions. Preserve explicit state paths, project facts and graph-referenced proof through dependency updates.
5. **Apply the engineering adapter.** Use `software-engineering` for engineering knowledge and execution. Its ontology holds the compatibility mapping to external lifecycle phases. Keep the original OntoLink source independent and unchanged.

## Host integration

When the host manages skills without a terminal, request and refresh the dependency through that capability and use the installation path it returns. Skills CLI availability is a host capability, not an installation assumption.

The engineering dependency resolver identifies installed paths by skill identity, including host-generated directory names and symlinks. It does not perform downloads or certify that an installation is current. Refreshing and reading the dependency are explicit start-of-session steps.

## Failure and compatibility handling

Installation and refresh require the host's actual network access and permissions. If either operation fails, report the exact condition and the known freshness of the available installation. Do not claim a successful update without an observed result.

If an update changes the mediator interface incompatibly, report the compatibility error and preserve project state. Use a deliberate adapter/dependency correction; do not introduce a copied or frozen coordinator as a fallback.

This directory remains instructions-only and contains a single `README.md`.
