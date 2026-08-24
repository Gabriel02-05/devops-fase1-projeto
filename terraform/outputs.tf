output "instance_id" {
  description = "ID da instância EC2 criada"
  value       = aws_instance.web_server.id
}

output "public_ip" {
  description = "IP Público da instância EC2"
  value       = aws_instance.web_server.public_ip
}
