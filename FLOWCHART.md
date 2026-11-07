# Flowchart — JSON-Based Log File Analyzer

```text
          +------------------+
          |      START       |
          +------------------+
                   |
                   v
          +------------------+
          | Load logs.json   |
          +------------------+
                   |
                   v
          +----------------------+
          | File and JSON valid? |
          +----------------------+
             | Yes         | No
             v             v
    +----------------+  +----------------+
    | Display menu   |  | Show error and |
    +----------------+  | stop program   |
             |          +----------------+
             v
    +----------------------+
    | Read user's choice   |
    +----------------------+
             |
             v
    +----------------------+
    | Run selected option  |
    | view/filter/search/  |
    | summary/save/reload  |
    +----------------------+
             |
             v
    +----------------------+
    | User selected Exit?  |
    +----------------------+
        | No          | Yes
        |             v
        |      +------------------+
        |      |       END        |
        |      +------------------+
        v
    Back to menu
```
