# Updating a Submodule in a Git Repository

Submodules allow you to keep a Git repository as a subdirectory of another Git repository. Here are the steps to update a submodule in your Git repository.

## Steps to Update a Submodule

1. **Navigate to the Submodule Directory**:
    ```bash
    cd path/to/submodule
    ```

2. **Fetch the Latest Changes**:
    ```bash
    git fetch
    ```

3. **Checkout the Desired Branch or Commit**:
    ```bash
    git checkout main
    ```

4. **Pull the Latest Changes**:
    ```bash
    git pull origin main
    ```

5. **Navigate Back to the Main Repository**:
    ```bash
    cd -
    ```

6. **Add the Updated Submodule**:
    ```bash
    git add path/to/submodule
    ```

7. **Commit the Changes**:
    ```bash
    git commit -m "Updated submodule to the latest version"
    ```

8. **Push the Changes**:
    ```bash
    git push
    ```

## Summary

By following these steps, you can ensure that your submodule is updated to the latest version. This process involves fetching and pulling the latest changes in the submodule, then committing and pushing these changes in the main repository.

## References

- [Git Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)