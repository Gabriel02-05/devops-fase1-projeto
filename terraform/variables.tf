variable "aws_region" {
  description = "Região da AWS onde os recursos serão criados"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "Tipo da instância EC2"
  type        = string
  default     = "t2.micro"
}

variable "environment" {
  description = "Ambiente de implantação"
  type        = string
  default     = "dev"
}
