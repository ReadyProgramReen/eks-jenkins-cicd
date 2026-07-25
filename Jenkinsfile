pipeline {
    agent any

    environment {
        AWS_REGION     = 'us-east-1'
        ECR_REPO       = '517169952856.dkr.ecr.us-east-1.amazonaws.com/tc2-flask-eks-app'
        IMAGE_TAG      = "${env.BUILD_NUMBER}"
        CLUSTER_NAME   = 'tc2-flask-eks-cluster'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                dir('app') {
                    sh "docker build -t ${ECR_REPO}:${IMAGE_TAG} ."
                }
            }
        }

        stage('Push to ECR') {
            steps {
                sh """
                    aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REPO}
                    docker push ${ECR_REPO}:${IMAGE_TAG}
                """
            }
        }

        stage('Deploy to EKS via Helm') {
            steps {
                sh """
                    aws eks update-kubeconfig --region ${AWS_REGION} --name ${CLUSTER_NAME}
                    helm upgrade --install flask-hello-world helm-chart/ \
                        --set image.repository=${ECR_REPO} \
                        --set image.tag=${IMAGE_TAG}
                """
            }
        }
    }

    post {
        success {
            echo "Deployment successful! Image tag: ${IMAGE_TAG}"
        }
        failure {
            echo "Pipeline failed — check logs above."
        }
    }
}