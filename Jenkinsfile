#!groovy


pipeline{
    agent {
        label 'trusty'
    }
    stages{
        stage("Build"){
            parallel {
                stage("Build Java"){
                    steps{
                        git branch: "${env.BRANCH_NAME}", credentialsId: 'fgreg-github', url: 'https://github.com/apache/incubator-sdap-nexusproto'
                    }
                }
                stage("Build Python"){
                    steps{
                        git branch: "${env.BRANCH_NAME}", credentialsId: 'fgreg-github', url: 'https://github.com/apache/incubator-sdap-nexusproto'
                    }
                }
            }
        }
    }
}