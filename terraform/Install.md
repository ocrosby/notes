# Installing Terraform

Install the HasiCorp tap, a repository of all their Homebrew packages.

```bash
brew tap hashicorp/tap
```

Install Terraform

```bash
brew install hashicorp/tap/terraform
```

To update to the latest version of Terraform, first update Homebrew.

```bash
brew update
```

Then, run the upgrade command to download and use the latest Terraform version.

```bash
brew upgrade hashicorp/tap/terraform
```

Verify the installation

```bash
terraform -help
```

Installing Terragrunt
```bash
brew install terragrunt
```