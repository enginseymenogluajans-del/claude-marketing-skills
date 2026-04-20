---
name: aws-skills
description: Use when the user asks about AWS infrastructure, CDK best practices, serverless architecture, Lambda functions, event-driven patterns, cost optimization, or AWS cloud deployment. Trigger keywords: AWS, CDK, CloudFormation, Lambda, serverless, S3, DynamoDB, API Gateway, event-driven, AWS cost, cloud infrastructure, AWS deployment.
---

# AWS Skills

## Overview
AWS CDK best practices, cost optimization, serverless and event-driven architecture patterns.

## CDK Best Practices

### Project Structure
```
my-cdk-app/
├── bin/
│   └── app.ts          # Entry point — instantiate stacks
├── lib/
│   ├── compute-stack.ts
│   ├── storage-stack.ts
│   └── shared/
│       └── constructs/  # Reusable L3 constructs
├── test/
│   └── app.test.ts
└── cdk.json
```

### L3 Construct (reusable pattern)
```typescript
import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as apigateway from 'aws-cdk-lib/aws-apigateway';

export class ApiFunction extends cdk.Construct {
  public readonly fn: lambda.Function;

  constructor(scope: cdk.Construct, id: string, props: { handler: string }) {
    super(scope, id);

    this.fn = new lambda.Function(this, 'Function', {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: props.handler,
      code: lambda.Code.fromAsset('lambda'),
      timeout: cdk.Duration.seconds(30),
      memorySize: 256,
      environment: {
        LOG_LEVEL: 'INFO',
      },
      // Cost optimization: ARM64 is 20% cheaper
      architecture: lambda.Architecture.ARM_64,
    });
  }
}
```

## Serverless Patterns

### Lambda + API Gateway
```typescript
const api = new apigateway.RestApi(this, 'Api', {
  defaultCorsPreflightOptions: {
    allowOrigins: apigateway.Cors.ALL_ORIGINS,
    allowMethods: apigateway.Cors.ALL_METHODS,
  },
  deployOptions: {
    stageName: 'prod',
    loggingLevel: apigateway.MethodLoggingLevel.INFO,
  },
});

const usersResource = api.root.addResource('users');
usersResource.addMethod('GET', new apigateway.LambdaIntegration(getUsers.fn));
usersResource.addMethod('POST', new apigateway.LambdaIntegration(createUser.fn));
```

### Event-Driven: SQS + Lambda
```typescript
import * as sqs from 'aws-cdk-lib/aws-sqs';
import * as lambdaEventSources from 'aws-cdk-lib/aws-lambda-event-sources';

const queue = new sqs.Queue(this, 'ProcessingQueue', {
  visibilityTimeout: cdk.Duration.seconds(300),
  deadLetterQueue: {
    queue: new sqs.Queue(this, 'DLQ'),
    maxReceiveCount: 3,
  },
});

processingFn.addEventSource(new lambdaEventSources.SqsEventSource(queue, {
  batchSize: 10,
  reportBatchItemFailures: true,  // partial batch success
}));
```

## Cost Optimization

| Strategy | Savings |
|----------|---------|
| Lambda ARM64 vs x86 | ~20% cheaper |
| Lambda right-sizing | Profile with Lambda Power Tuning |
| S3 Intelligent-Tiering | Auto-moves cold data |
| DynamoDB on-demand → provisioned | Up to 70% for stable workloads |
| Reserved Instances (1yr) | Up to 40% off EC2 |
| Spot Instances for batch | Up to 90% off |

### Lambda Power Tuning (cost + speed)
```bash
# Deploy and run Lambda Power Tuning tool
# github.com/alexcasalboni/aws-lambda-power-tuning
aws stepfunctions start-execution \
  --state-machine-arn <power-tuning-arn> \
  --input '{"lambdaARN":"<fn-arn>","powerValues":[128,256,512,1024],"num":10}'
```

## Output Format
- CDK stack code (TypeScript)
- Architecture diagram (ASCII)
- Cost estimate for the proposed architecture
- Deployment commands: `cdk synth && cdk deploy`
