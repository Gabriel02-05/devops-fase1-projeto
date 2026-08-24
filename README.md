# 🚀 Projeto DevOps - Fase 1: CI & IaC Pipeline

Repositório acadêmico voltado à implementação de uma esteira automatizada de **Integração Contínua (CI)** e provisionamento de **Infraestrutura como Código (IaC)**, garantindo entregas consistentes, testes automatizados e ambientes reproduzíveis.

---

## 📌 1.a) Descrição do Projeto, Objetivos e Requisitos

### Descrição
Implementação de uma esteira de automação DevOps para um microsserviço Python, integrando validação contínua de software via **GitHub Actions** e gerenciamento declarativo de infraestrutura em nuvem via **Terraform**.

### Objetivos
* **Eliminar o Provisionamento Manual (Anti-ClickOps):** Automatizar a criação e validação de recursos em nuvem.
* **Garantia de Qualidade de Software:** Executar suítes de testes unitários automatizados a cada alteração no código.
* **Padronização e Reprodutibilidade:** Garantir ambientes de infraestrutura idênticos, auditáveis e versionados via código.

### Requisitos Técnicos
* **Controle de Versão:** Repositório Git estruturado com versionamento semântico.
* **Pipeline de CI:** Execução automatizada de testes e checagem estática em nuvem (*GitHub Actions*).
* **Validação de IaC:** Verificação sintática e de boas práticas de scripts HCL com *Terraform*.
* **Infraestrutura AWS:** Definição de recursos gerenciados via Terraform no ecossistema AWS Free Tier.

---

## 🔄 1.b) Plano de Integração Contínua (CI)

### Estratégia de Branching (GitFlow Simplificado)
* `main`: Ramo estável, protegido e pronto para produção/homologação.
* `feature/*`: Ramos temporários destinados ao desenvolvimento isolado de novas funcionalidades e correções.

### Gatilhos da Esteira (Triggers)
A pipeline de CI é acionada automaticamente nos seguintes eventos:
* `push` direcionado às branches `main` e `feature/*`.
* `pull_request` aberto contra a branch `main`.

### Barreiras de Qualidade (Quality Gates)
O merge e a aprovação de builds são bloqueados caso ocorra:
1. **Falha na suíte de testes:** Qualquer asserção quebrada na execução do `pytest`.
2. **Inconformidade de IaC:** Erros de sintaxe ou formatação detectados pelo `terraform fmt -check`.
3. **Erros de Dependências:** Incompatibilidades durante a resolução do `requirements.txt`.

---

## ☁️ 1.c) Especificação da Infraestrutura

* **Provedor Cloud:** Amazon Web Services (AWS) — Camada Gratuita (*Free Tier*).
* **Região Principal:** `us-east-1` (Norte da Virgínia).

| Recurso | Tipo / Detalhe | Finalidade |
| :--- | :--- | :--- |
| **Compute (EC2)** | `t2.micro` (Ubuntu Server 22.04 LTS) | Hospedagem da aplicação/microsserviço |
| **Rede (VPC)** | Default VPC com Subnet Pública | Roteamento e conectividade externa |
| **Segurança (SG)** | Ingress: 22 (SSH), 80 (HTTP), 443 (HTTPS) | Controle de acesso ao tráfego de rede |
| **Armazenamento de Estado** | AWS S3 Bucket | Armazenamento seguro do estado remoto (`.tfstate`) |

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.11
* **Testes Automatizados:** PyTest
* **CI/CD:** GitHub Actions
* **IaC:** HashiCorp Terraform
* **Cloud:** AWS (EC2, S3, VPC, Security Group)