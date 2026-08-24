# devops-fase1-projeto
1.a) Descrição do Projeto, Objetivos e Requisitos

Descrição: Implementação de uma esteira inicial de cultura e automação DevOps para um microserviço, utilizando práticas de Integração Contínua (CI) e Infraestrutura como Código (IaC).

Objetivos:

Eliminar o provisionamento manual de servidores (ClickOps).

Garantir a integridade do código através de testes automatizados a cada commit.

Garantir ambientes reproduzíveis e padronizados utilizando infraestrutura declarativa.

Requisitos:

Repositório Git com branch principal protegida.

Testes unitários automatizados executados na nuvem.

Validação sintática e estrutural dos scripts de infraestrutura.

Script IaC para criação de instância EC2 e Security Group na AWS.

1.b) Plano de Integração Contínua (CI)

Estratégia de Branching: GitFlow Simplificado.

Branch main: Código estável e validado.

Branches feature/*: Desenvolvimento de novas funcionalidades.

Gatilhos (Triggers): A esteira de CI roda automaticamente em:

Todo push realizado na branch main ou feature/*.

Abertura de qualquer pull_request direcionado à main.

Quality Gates (Barreiras de Qualidade): O merge para a branch main é bloqueado se:

Qualquer teste unitário falhar.

O linter apontar erros de padronização de código.

Os scripts do Terraform possuírem erros de sintaxe ou formatação.

1.c) Especificação da Infraestrutura Necessária

Provedor Cloud: AWS (Amazon Web Services) - Camada Gratuita (Free Tier).

Serviços:

EC2: 1x Instância t2.micro rodando Ubuntu Server 22.04 LTS.

VPC e Subnet: VPC padrão com suporte a IP Público.

Security Group: Liberação das portas 22 (SSH - apenas manutenção), 80 (HTTP) e 443 (HTTPS).

Armazenamento de Estado: AWS S3 Bucket para armazenamento remoto do arquivo de estado (.tfstate).