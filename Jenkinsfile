pipeline {
  agent any
  stages {
    stage('检出代码') {
      steps {
        checkout([
          $class: 'GitSCM',
          branches: [[name: env.GIT_BUILD_REF]],
          userRemoteConfigs: [[
            url: env.GIT_REPO_URL,
            credentialsId: env.CREDENTIALS_ID
          ]]])
        }
      }
      stage('安装依赖') {
        steps {
          echo '安装依赖中...'
          sh 'apt-get install -y python3.7'
          sh 'pip3.7 install --upgrade pip'
          sh 'pip3.7 install --upgrade poetry'
          echo '安装依赖完成.'
        }
      }
      stage('配置仓库') {
        steps {
          echo '配置仓库中...'
          sh "poetry config repositories.Coding ${REPOSITORIES_CODING}"
          sh "poetry config virtualenvs.create false"
          echo '配置仓库完成.'
        }
      }
      stage('发布版本') {
        steps {
          echo '发布版本中...'
          sh 'poetry build -f wheel'
          archiveArtifacts(artifacts: 'dist/*', allowEmptyArchive: true)
          sh 'poetry publish -u __token__ -p ${PYPI_API_TOKEN}'
          sh 'poetry publish -r Coding -u ${CODING_API_USER} -p ${CODING_API_TOKEN}'
          echo '发布版本完成.'
        }
      }
    }
  }