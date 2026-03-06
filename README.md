# Backend Roadmap Challenge
**8 Phases · 45 Projects**

This is a personal challenge to build backend infrastructure from scratch. No frameworks doing the hard part or tutorials to follow; just specs and figuring it out. In a world where AI has caused an extreme increase in shipping velocity, I believe having a strong base is more important than ever. Each project targets a layer that's usually hidden behind libraries, frameworks, or built-in tools that we often take for granted.

---

## Phases

| Phase | Focus |
|-------|-------|
| 01 | Internet Fundamentals
| 02 | Language & Version Control
| 03 | Relational Databases
| 04 | NoSQL & Scaling
| 05 | APIs & Caching
| 06 | Security, Testing & CI/CD
| 07 | Architecture & Messaging
| 08 | Real-Time & Scale

---

## Projects

### Phase 01 — Internet Fundamentals
- **01. Network Packet Tracer** — Raw socket capture, Ethernet/IP/TCP/UDP/DNS parsing from scratch
- **02. HTTP/1.1 Server** — TCP socket, raw HTTP parsing, keep-alive, chunked encoding
- **03. DNS Resolver** — Recursive resolution, root servers, TTL caching
- **04. Domain & Hosting Simulator** — DNS to IP mapping, virtual hosts, SSL termination
- **05. HTML/CSS Renderer** — Lexer, DOM tree, CSS cascade, box model

### Phase 02 — Language & Version Control
- **06. Package Manager Clone** — Dependency graphs, semver, lockfiles, registry APIs
- **07. Async Task Scheduler** — Event loop, microtask queue, Promise-like construct
- **08. Git Clone** — Blob/tree/commit model, SHA storage, diff, branch
- **09. GitHub/GitLab CLI** — OAuth, pagination, rate limiting, webhooks

### Phase 03 — Relational Databases
- **10. PostgreSQL Client** — Wire protocol, MD5/SCRAM auth, result parsing
- **11. SQL Query Engine** — Lexer, AST, query planner, cost-based optimizer
- **12. B-Tree** — Insert, delete, range queries, disk page management
- **13. ACID Transaction Manager** — WAL, MVCC, lock management, crash recovery
- **14. ORM** — Model definition, migrations, query builder, N+1 detection
- **15. Database Profiler** — EXPLAIN hooking, slow query tracking, flamegraphs

### Phase 04 — NoSQL & Scaling
- **16. Document DB** — JSON store, query operators, aggregation pipeline, indexes
- **17. Key-Value Store** — In-memory, TTL, RDB + AOF persistence, pub/sub
- **18. Graph DB** — Vertex/edge storage, BFS/DFS/Dijkstra, Cypher-style queries
- **19. Time-Series DB** — Columnar storage, delta/RLE compression, downsampling
- **20. Sharding System** — Consistent hashing, virtual nodes, rebalancing
- **21. Replication System** — WAL shipping, failover, replication lag
- **22. CAP Theorem Demonstrator** — Network partition simulation, CP vs AP tradeoffs

### Phase 05 — APIs & Caching
- **23. RESTful Framework** — Routing, middleware pipeline, content negotiation, HATEOAS
- **24. GraphQL Server** — Schema parsing, resolvers, DataLoader, subscriptions
- **25. gRPC Service** — Protobuf, HTTP/2 streams, deadlines, bidirectional streaming
- **26. CDN Simulator** — Edge caching, cache-control, stale-while-revalidate
- **27. Multi-Level Cache** — L1/L2/L3, write-through/back, stampede prevention

### Phase 06 — Security, Testing & CI/CD
- **28. Auth System** — JWT signing, OAuth 2.0 + PKCE, SAML SP/IdP, key rotation
- **29. OWASP Top 10** — SQLi, XSS, SSRF, IDOR — implement then mitigate
- **30. TLS Server** — TLS 1.3 handshake, ECDH, cipher negotiation, X.509 parsing
- **31. Testing Framework** — Test runner, mocks, property-based testing, mutation testing
- **32. CI/CD Pipeline** — Git-triggered jobs, artifact caching, blue/green + canary deploys

### Phase 07 — Architecture & Messaging
- **33. Design Patterns Library** — All GoF patterns + distributed: saga, outbox, circuit breaker
- **34. Microservices** — Service discovery, API gateway, distributed tracing
- **35. CQRS / Event Sourcing** — Event store, projections, eventual consistency, replay
- **36. Message Queue** — Durable queues, consumer groups, backpressure, DLQ
- **37. Kafka Clone** — Log segments, partitions, consumer offsets, leader election

### Phase 08 — Real-Time & Scale
- **38. WebSocket Server** — Upgrade handshake, framing, heartbeats, pub/sub fan-out
- **39. Nginx Clone** — Event-driven reverse proxy, upstream pooling, load balancing
- **40. Container Runtime** — Linux namespaces, cgroups, overlay FS, container networking
- **41. Monitoring System** — Metrics collection, TSDB, alerting, distributed tracing
- **42. Circuit Breakers** — Closed/open/half-open states, bulkheads, exponential backoff
- **43. Load Balancer** — L4/L7, sticky sessions, health checks, A/B traffic splitting

---

## Build Philosophy

- Start naive. Make it work first, don't pre-architect.
- No premature optimization.
- Add complexity only when/if the naive version fails.
- Document every decision and why.