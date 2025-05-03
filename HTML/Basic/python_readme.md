```mermaid
flowchart TD
  %% Module 1
  subgraph M1 [Module 1: Introduction & Setup]
    M1A[What is Python?]
    M1B[Installing Python]
    M1C[Running Python Code]
  end

  %% Module 2
  subgraph M2 [Module 2: Python Basics]
    M2A[Syntax & Semantics]
    M2B[Data Types & Variables]
    M2C[Operators]
    M2D[Control Flow]
    M2E[Comprehensions]
    M2F[Built-in Functions & Modules]
  end

  %% Module 3
  subgraph M3 [Module 3: Data Structures]
    M3A[Lists & Tuples]
    M3B[Sets]
    M3C[Dictionaries]
    M3D[Advanced Collections]
    M3E[DS Performance]
  end

  %% Module 4
  subgraph M4 [Module 4: Functions & Scripting]
    M4A[Defining Functions]
    M4B[Lambda & HOFs]
    M4C[Docstrings & Annotations]
    M4D[Scripting Essentials]
    M4E[Packaging Scripts]
  end

  %% Module 5
  subgraph M5 [Module 5: Object-Oriented Programming]
    M5A[Classes & Instances]
    M5B[Encapsulation]
    M5C[Inheritance]
    M5D[Polymorphism]
    M5E[Magic Methods]
    M5F[Class/Static Methods]
    M5G[Design Patterns (Intro)]
  end

  %% Module 6
  subgraph M6 [Module 6: File Handling]
    M6A[Text Files]
    M6B[Binary Files]
    M6C[CSV & JSON]
    M6D[Path Handling]
  end

  %% Module 7
  subgraph M7 [Module 7: Error & Exception Handling]
    M7A[Errors vs Exceptions]
    M7B[Try/Except/Else/Finally]
    M7C[Catching Specific]
    M7D[Raising Exceptions]
    M7E[Custom Exception Classes]
    M7F[Best Practices]
  end

  %% Module 8
  subgraph M8 [Module 8: Modules, Packages & Virtual Envs]
    M8A[Creating & Importing]
    M8B[Packages]
    M8C[Std Library Overview]
    M8D[Third-Party & venv]
    M8E[Setup.py / pyproject.toml]
  end

  %% Module 9
  subgraph M9 [Module 9: Testing & Debugging]
    M9A[Debugging Tools]
    M9B[Writing Tests]
    M9C[Test Coverage]
  end

  %% Module 10
  subgraph M10 [Module 10: Advanced Scripting Topics]
    M10A[Regular Expressions]
    M10B[OS & Subprocess]
    M10C[Concurrency & Async]
    M10D[Working with APIs]
    M10E[Logging & Config]
  end

  %% Module 11
  subgraph M11 [Module 11: Final Project & Best Practices]
    M11A[Project Planning]
    M11B[Code Style & Linters]
    M11C[Documentation]
    M11D[Version Control & CI/CD]
  end

  %% Flow
  M1 --> M2 --> M3 --> M4 --> M5 --> M6 --> M7 --> M8 --> M9 --> M10 --> M11
```