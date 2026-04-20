---
name: software-arch
description: Use when the user asks to design software architecture, review architecture decisions, apply Clean Architecture, SOLID principles, design patterns, or system design. Use for high-level design before implementation. Trigger keywords: architecture, software design, Clean Architecture, SOLID, design pattern, system design, refactor architecture, dependency injection, domain model.
---

# Software Architecture Skill

## Overview
Apply Clean Architecture, SOLID principles, and comprehensive software design best practices to design systems that are maintainable, testable, and extensible.

## Clean Architecture Layers

```
┌─────────────────────────────────┐
│         Frameworks & Drivers    │  ← DB, UI, Web, External APIs
├─────────────────────────────────┤
│      Interface Adapters         │  ← Controllers, Presenters, Gateways
├─────────────────────────────────┤
│       Application Layer         │  ← Use Cases, Application Services
├─────────────────────────────────┤
│         Domain Layer            │  ← Entities, Domain Services, Value Objects
└─────────────────────────────────┘
       Dependency Rule: always points inward
```

## SOLID Principles Checklist

**S — Single Responsibility**: Each class has one reason to change
```python
# BAD: UserService handles auth + email + DB
# GOOD: separate AuthService, EmailService, UserRepository
```

**O — Open/Closed**: Open for extension, closed for modification
```python
class Notifier(ABC):
    @abstractmethod
    def notify(self, message: str): ...

class EmailNotifier(Notifier): ...
class SlackNotifier(Notifier): ...
```

**L — Liskov Substitution**: Subclasses must be substitutable for base class
**I — Interface Segregation**: Small, focused interfaces over large ones
**D — Dependency Inversion**: Depend on abstractions, not concretions

## Design Patterns (by problem type)

| Problem | Pattern |
|---------|---------|
| Object creation | Factory, Builder, Singleton |
| Object structure | Adapter, Decorator, Facade |
| Object behavior | Strategy, Observer, Command |
| Distributed | CQRS, Event Sourcing, Saga |

## Architecture Decision Process

1. Identify quality attributes (performance, scalability, maintainability)
2. List constraints (team size, timeline, existing tech)
3. Enumerate options with trade-offs
4. Select and document with ADR (Architecture Decision Record)

### ADR Template
```markdown
# ADR-001: [Decision Title]
**Status**: Accepted
**Context**: [Why this decision is needed]
**Decision**: [What was decided]
**Consequences**: [Trade-offs accepted]
```

## Dependency Injection Example
```python
# Interface (Domain layer)
class UserRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: str) -> User: ...

# Implementation (Infrastructure layer)
class PostgresUserRepository(UserRepository):
    def find_by_id(self, id: str) -> User:
        # DB query here
        ...

# Use Case (Application layer) — depends on abstraction
class GetUserUseCase:
    def __init__(self, repo: UserRepository):
        self.repo = repo
```

## Output Format
- Architecture diagram (ASCII or description)
- Layer breakdown with responsibilities
- Key design decisions + rationale
- Code structure recommendation (folder layout)
