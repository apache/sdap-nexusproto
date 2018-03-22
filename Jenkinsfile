#!groovy


pipeline{
    agent {
        label 'trusty'
    }
    stages{
        stage("Build"){
            steps{
                git branch: "${env.BRANCH_NAME}", credentialsId: 'fgreg-github', url: 'https://github.com/apache/incubator-sdap-nexusproto'
                sh './gradlew clean build'
            }
        }
        stage("Assemble"){
            steps{
                sh './gradlew assemble'
                archiveArtifacts artifacts: '**/nexusproto-*.jar **/nexusproto-*.tar.gz', fingerprint: true, onlyIfSuccessful: true
            }
        }
    }
}