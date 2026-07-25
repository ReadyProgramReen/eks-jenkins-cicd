resource "tls_private_key" "jenkins" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "jenkins" {
  key_name   = "${var.project_name}-jenkins-key"
  public_key = tls_private_key.jenkins.public_key_openssh
}

resource "local_file" "jenkins_private_key" {
  content         = tls_private_key.jenkins.private_key_pem
  filename        = "${path.module}/jenkins-key.pem"
  file_permission = "0400"
}