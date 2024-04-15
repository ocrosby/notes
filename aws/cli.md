# AWS CLI

## Configuration and credentials precense

Credentials and configuration settings are located in multiple places.

The IAM Identity Center configuration settings are stored in the ~/.aws/config file.

The credentials file is located at ~/.aws/credentials.  

To set things up initially you can use the `aws configure` command.

```bash
aws configure
```

## Configuration Envirionment Variables

You can also set the following environment variables to configure the AWS CLI:

```bash
export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
export AWS_DEFAULT_REGION=us-west-2
```

## AWS CLI supported environment variables

The AWS CLI supports the following environment variables.

AWS_ACCESS_KEY_ID
: Specifies an AWS access key associated with an IAM account.

If defined, this environment variable overrides the value for the profile setting aws_access_key_id. You can't specify the access key ID by using a command line option.

AWS_CA_BUNDLE
: Specifies the path to a certificate bundle to use for HTTPS certificate validation.

If defined, this environment variable overrides the value for the profile setting ca_bundle. You can override this environment variable by using the --ca-bundle command line parameter.

AWS_CLI_AUTO_PROMPT
: Enables the auto-prompt for the AWS CLI version 2. There are two settings that can be used:

* on uses the full auto-prompt mode each time you attempt to run an aws command. This includes pressing ENTER after both a complete command or incomplete command.
* on-partial uses partial auto-prompt mode. If a command is incomplete or cannot be run due to client-side validation errors, auto-prompt is used. This mode is useful if you have pre-existing scripts, runbooks, or you only want to be auto-prompted for commands you are unfamiliar with rather than prompted on every command.

If defined, this environment variable overrides the value for the cli_auto_prompt profile setting. You can override this environment variable by using the --cli-auto-prompt and --no-cli-auto-prompt command line parameters.

For information on the AWS CLI version 2 auto-prompt feature, see Have the AWS CLI prompt you for commands.

AWS_CLI_FILE_ENCODING
: Specifies the encoding used for text files. By default encoding matches your locale. To set encoding different from the locale, use the aws_cli_file_encoding environment variable. For example, if you use Windows with default encoding CP1252, setting aws_cli_file_encoding=UTF-8 sets the CLI to open text files using UTF-8.

AWS_CONFIG_FILE
: Specifies the location of the file that the AWS CLI uses to store configuration profiles. The default path is ~/.aws/config.

You can't specify this value in a named profile setting or by using a command line parameter.

AWS_DATA_PATH
: A list of additional directories to check outside of the built-in search path of ~/.aws/models when loading AWS CLI data. Setting this environment variable indicates additional directories to check first before falling back to the built-in search path. Multiple entries should be separated with the os.pathsep character, which is : on Linux or macOS and ; on Windows.

AWS_DEFAULT_OUTPUT
: Specifies the output format to use.

If defined, this environment variable overrides the value for the profile setting output. You can override this environment variable by using the --output command line parameter.

AWS_DEFAULT_REGION
: The Default region name identifies the AWS Region whose servers you want to send your requests to by default. This is typically the Region closest to you, but it can be any Region. For example, you can type us-west-2 to use US West (Oregon). This is the Region that all later requests are sent to, unless you specify otherwise in an individual command.

Note
You must specify an AWS Region when using the AWS CLI, either explicitly or by setting a default Region. For a list of the available Regions, see Regions and Endpoints. The Region designators used by the AWS CLI are the same names that you see in AWS Management Console URLs and service endpoints.

AWS_EC2_METADATA_DISABLED
: Disables the use of the Amazon EC2 instance metadata service (IMDS).

If set to true, user credentials or configuration (like the Region) are not requested from IMDS.

AWS_ENDPOINT_URL
: Specifies the endpoint that is used for all service requests.

Endpoint configuration settings are located in multiple places, such as the system or user environment variables, local AWS configuration files, or explicitly declared on the command line as a parameter. The AWS CLI endpoint configuration settings take precedence in the following order:

* The --endpoint-url command line option.
* If enabled, the AWS_IGNORE_CONFIGURED_ENDPOINT_URLS global endpoint environment variable or profile setting ignore_configure_endpoint_urls to ignore custom endpoints.
* The value provided by a service-specific environment variable AWS_ENDPOINT_URL_<SERVICE>, such as AWS_ENDPOINT_URL_DYNAMODB.
* The values provided by the AWS_USE_DUALSTACK_ENDPOINT, AWS_USE_FIPS_ENDPOINT, and AWS_ENDPOINT_URL environment variables.
* The service-specific endpoint value provided by the endpoint_url setting within a services section of the shared config file.
* The value provided by the endpoint_url setting within a profile of the shared config file.
* use_dualstack_endpoint, use_fips_endpoint, and endpoint_url settings.
* Any default endpoint URL for the respective AWS service is used last. For a list of the standard service endpoints available in each Region, see AWS Regions and Endpoints in the Amazon Web Services General Reference.

AWS_ENDPOINT_URL_<SERVICE>
: Specifies a custom endpoint that is used for a specific service, where <SERVICE> is replaced with the AWS service identifier. For example, Amazon DynamoDB has a serviceId of DynamoDB. For this service, the endpoint URL environment variable is AWS_ENDPOINT_URL_DYNAMODB.

For a list of all service-specific environment variables, see List of service-specific identifiers.

Endpoint configuration settings are located in multiple places, such as the system or user environment variables, local AWS configuration files, or explicitly declared on the command line as a parameter. The AWS CLI endpoint configuration settings take precedence in the following order:

* The --endpoint-url command line option.
* If enabled, the AWS_IGNORE_CONFIGURED_ENDPOINT_URLS global endpoint environment variable or profile setting ignore_configure_endpoint_urls to ignore custom endpoints.
* The value provided by a service-specific environment variable AWS_ENDPOINT_URL_<SERVICE>, such as AWS_ENDPOINT_URL_DYNAMODB.
* The values provided by the AWS_USE_DUALSTACK_ENDPOINT, AWS_USE_FIPS_ENDPOINT, and AWS_ENDPOINT_URL environment variables.
* The service-specific endpoint value provided by the endpoint_url setting within a services section of the shared config file.
* The value provided by the endpoint_url setting within a profile of the shared config file.
* use_dualstack_endpoint, use_fips_endpoint, and endpoint_url settings.
* Any default endpoint URL for the respective AWS service is used last. For a list of the standard service endpoints available in each Region, see AWS Regions and Endpoints in the Amazon Web Services General Reference.

AWS_IGNORE_CONFIGURED_ENDPOINT_URLS
: If enabled, the AWS CLI ignores all custom endpoint configurations. Valid values are true and false.

Endpoint configuration settings are located in multiple places, such as the system or user environment variables, local AWS configuration files, or explicitly declared on the command line as a parameter. The AWS CLI endpoint configuration settings take precedence in the following order:

* The --endpoint-url command line option.
* If enabled, the AWS_IGNORE_CONFIGURED_ENDPOINT_URLS global endpoint environment variable or profile setting ignore_configure_endpoint_urls to ignore custom endpoints.
* The value provided by a service-specific environment variable AWS_ENDPOINT_URL_<SERVICE>, such as AWS_ENDPOINT_URL_DYNAMODB.
* The values provided by the AWS_USE_DUALSTACK_ENDPOINT, AWS_USE_FIPS_ENDPOINT, and AWS_ENDPOINT_URL environment variables.
* The service-specific endpoint value provided by the endpoint_url setting within a services section of the shared config file.
* The value provided by the endpoint_url setting within a profile of the shared config file.
* use_dualstack_endpoint, use_fips_endpoint, and endpoint_url settings.
* Any default endpoint URL for the respective AWS service is used last. For a list of the standard service endpoints available in each Region, see AWS Regions and Endpoints in the Amazon Web Services General Reference.

AWS_MAX_ATTEMPTS
: Specifies a value of maximum retry attempts the AWS CLI retry handler uses, where the initial call counts toward the value that you provide. For more information on retries, see AWS CLI retries.

If defined, this environment variable overrides the value for the profiles setting max_attempts.

AWS_METADATA_SERVICE_NUM_ATTEMPTS
: When attempting to retrieve credentials on an Amazon EC2 instance that has been configured with an IAM role, the AWS CLI attempts to retrieve credentials once from the instance metadata service before stopping. If you know your commands will run on an Amazon EC2 instance, you can increase this value to make AWS CLI retry multiple times before giving up.

AWS_METADATA_SERVICE_TIMEOUT
: The number of seconds before a connection to the instance metadata service should time out. When attempting to retrieve credentials on an Amazon EC2 instance that is configured with an IAM role, a connection to the instance metadata service times out after 1 second by default. If you know you're running on an Amazon EC2 instance with an IAM role configured, you can increase this value if needed.

AWS_PAGER
: Specifies the pager program used for output. By default, AWS CLI version 2 returns all output through your operating system’s default pager program.

To disable all use of an external paging program, set the variable to an empty string.

If defined, this environment variable overrides the value for the profile setting cli_pager.

AWS_PROFILE
: Specifies the name of the AWS CLI profile with the credentials and options to use. This can be the name of a profile stored in a credentials or config file, or the value default to use the default profile.

If defined, this environment variable overrides the behavior of using the profile named [default] in the configuration file. You can override this environment variable by using the --profile command line parameter.

AWS_REGION
: The AWS SDK compatible environment variable that specifies the AWS Region to send the request to.

If defined, this environment variable overrides the values in the environment variable AWS_DEFAULT_REGION and the profile setting region. You can override this environment variable by using the --region command line parameter.

AWS_RETRY_MODE
: Specifies which retry mode AWS CLI uses. There are three retry modes available: legacy (default), standard, and adaptive. For more information on retries, see AWS CLI retries.

If defined, this environment variable overrides the value for the profiles setting retry_mode.

AWS_ROLE_ARN
: Specifies the Amazon Resource Name (ARN) of an IAM role with a web identity provider that you want to use to run the AWS CLI commands.

Used with the AWS_WEB_IDENTITY_TOKEN_FILE and AWS_ROLE_SESSION_NAME environment variables.

If defined, this environment variable overrides the value for the profile setting role_arn. You can't specify a role session name as a command line parameter.

Note
This environment variable only applies to an assumed role with web identity provider it does not apply to the general assume role provider configuration.

For more information on using web identities, see Assume role with web identity.

AWS_ROLE_SESSION_NAME
: Specifies the name to attach to the role session. This value is provided to the RoleSessionName parameter when the AWS CLI calls the AssumeRole operation, and becomes part of the assumed role user ARN: arn:aws:sts::123456789012:assumed-role/role_name/role_session_name. This is an optional parameter. If you do not provide this value, a session name is generated automatically. This name appears in AWS CloudTrail logs for entries associated with this session.

If defined, this environment variable overrides the value for the profile setting role_session_name.

Used with the AWS_ROLE_ARN and AWS_WEB_IDENTITY_TOKEN_FILE environment variables.

For more information on using web identities, see Assume role with web identity.

Note
This environment variable only applies to an assumed role with web identity provider it does not apply to the general assume role provider configuration.

AWS_SECRET_ACCESS_KEY
: Specifies the secret key associated with the access key. This is essentially the "password" for the access key.

If defined, this environment variable overrides the value for the profile setting aws_secret_access_key. You can't specify the secret access key ID as a command line option.

AWS_SESSION_TOKEN
: Specifies the session token value that is required if you are using temporary security credentials that you retrieved directly from AWS STS operations. For more information, see the Output section of the assume-role command in the AWS CLI Command Reference.

If defined, this environment variable overrides the value for the profile setting aws_session_token.

AWS_SHARED_CREDENTIALS_FILE
: Specifies the location of the file that the AWS CLI uses to store access keys. The default path is ~/.aws/credentials.

You can't specify this value in a named profile setting or by using a command line parameter.

AWS_USE_DUALSTACK_ENDPOINT
: Enables the use of dual-stack endpoints to send AWS requests. To learn more about dual-stack endpoints, which support both IPv4 and IPv6 traffic, see Using Amazon S3 dual-stack endpoints in the Amazon Simple Storage Service User Guide. Dual-stack endpoints are available for some services in some regions. If a dual-stack endpoint does not exist for the service or AWS Region, the request fails. This is disabled by default.

Endpoint configuration settings are located in multiple places, such as the system or user environment variables, local AWS configuration files, or explicitly declared on the command line as a parameter. The AWS CLI endpoint configuration settings take precedence in the following order:

* The --endpoint-url command line option.
* If enabled, the AWS_IGNORE_CONFIGURED_ENDPOINT_URLS global endpoint environment variable or profile setting ignore_configure_endpoint_urls to ignore custom endpoints.
* The value provided by a service-specific environment variable AWS_ENDPOINT_URL_<SERVICE>, such as AWS_ENDPOINT_URL_DYNAMODB.
* The values provided by the AWS_USE_DUALSTACK_ENDPOINT, AWS_USE_FIPS_ENDPOINT, and AWS_ENDPOINT_URL environment variables.
* The service-specific endpoint value provided by the endpoint_url setting within a services section of the shared config file.
* The value provided by the endpoint_url setting within a profile of the shared config file.
* use_dualstack_endpoint, use_fips_endpoint, and endpoint_url settings.
* Any default endpoint URL for the respective AWS service is used last. For a list of the standard service endpoints available in each Region, see AWS Regions and Endpoints in the Amazon Web Services General Reference.

AWS_USE_FIPS_ENDPOINT
: Some AWS services offer endpoints that support Federal Information Processing Standard (FIPS) 140-2 in some AWS Regions. When the AWS service supports FIPS, this setting specifies what FIPS endpoint the AWS CLI should use . Unlike standard AWS endpoints, FIPS endpoints use a TLS software library that complies with FIPS 140-2. These endpoints might be required by enterprises that interact with the United States government.

If this setting is enabled, but a FIPS endpoint does not exist for the service in your AWS Region, the AWS command may fail. In this case, manually specify the endpoint to use in the command using the --endpoint-url option or use service-specific endpoints.

For more information on specifying FIPS endpoints by AWS Region, see FIPS Endpoints by Service.

Endpoint configuration settings are located in multiple places, such as the system or user environment variables, local AWS configuration files, or explicitly declared on the command line as a parameter. The AWS CLI endpoint configuration settings take precedence in the following order:

* The --endpoint-url command line option.
* If enabled, the AWS_IGNORE_CONFIGURED_ENDPOINT_URLS global endpoint environment variable or profile setting ignore_configure_endpoint_urls to ignore custom endpoints.
* The value provided by a service-specific environment variable AWS_ENDPOINT_URL_<SERVICE>, such as AWS_ENDPOINT_URL_DYNAMODB.
* The values provided by the AWS_USE_DUALSTACK_ENDPOINT, AWS_USE_FIPS_ENDPOINT, and AWS_ENDPOINT_URL environment variables.
* The service-specific endpoint value provided by the endpoint_url setting within a services section of the shared config file.
* The value provided by the endpoint_url setting within a profile of the shared config file.
* use_dualstack_endpoint, use_fips_endpoint, and endpoint_url settings.
* Any default endpoint URL for the respective AWS service is used last. For a list of the standard service endpoints available in each Region, see AWS Regions and Endpoints in the Amazon Web Services General Reference.

AWS_WEB_IDENTITY_TOKEN_FILE
: Specifies the path to a file that contains an OAuth 2.0 access token or OpenID Connect ID token that is provided by an identity provider. The AWS CLI loads the contents of this file and passes it as the WebIdentityToken argument to the AssumeRoleWithWebIdentity operation.

Used with the AWS_ROLE_ARN and AWS_ROLE_SESSION_NAME environment variables.

If defined, this environment variable overrides the value for the profile setting web_identity_token_file.

For more information on using web identities, see Assume role with web identity.

Note
This environment variable only applies to an assumed role with web identity provider it does not apply to the general assume role provider configuration.


## Common CLI Commands

List all S3 buckets

```bash
aws s3 ls
```

List all ec2 instances

```bash
aws ec2 describe-instances
```
