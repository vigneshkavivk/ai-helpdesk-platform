pipeline {
    agent any

    environment {
        DOCKER_REPO = "vigneshkavi"     // your dockerhub username
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/vigneshkavivk/ai-helpdesk-platform.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh '''
                docker build -t $DOCKER_REPO/auth-service:latest services/auth-service
                docker build -t $DOCKER_REPO/ai-service:latest services/ai-service
                docker build -t $DOCKER_REPO/ticket-service:latest services/ticket-service
                docker build -t $DOCKER_REPO/notification-service:latest services/notification-service
                '''
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh '''
                    echo $PASS | docker login -u $USER --password-stdin
                    '''
                }
            }
        }

        stage('Push Docker Images') {
            steps {
                sh '''
                docker push $DOCKER_REPO/auth-service:latest
                docker push $DOCKER_REPO/ai-service:latest
                docker push $DOCKER_REPO/ticket-service:latest
                docker push $DOCKER_REPO/notification-service:latest
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl apply -f kubernetes/auth-deployment.yaml
                kubectl apply -f kubernetes/ai-deployment.yaml
                kubectl apply -f kubernetes/ticket-deployment.yaml
                kubectl apply -f kubernetes/notification-deployment.yaml
                kubectl apply -f kubernetes/services.yaml
                kubectl apply -f kubernetes/ingress.yaml
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                kubectl get pods
                kubectl get svc
                '''
            }
        }

    }
}
