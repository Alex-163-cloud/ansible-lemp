# Ansible LEMP & Infrastructure Automation

[![Pipeline](https://gitlab.com/vladimir_vgb/ansible-lemp/badges/main/pipeline.svg)](https://gitlab.com/vladimir_vgb/ansible-lemp/-/pipelines)
[![Ansible](https://img.shields.io/badge/Ansible-2.21-blue)](https://www.ansible.com/)
[![Molecule](https://img.shields.io/badge/Molecule-26.10-brightgreen)](https://molecule.readthedocs.io/)
[![Docker](https://img.shields.io/badge/Docker-ready-blue)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.14-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## 🇷🇺 Русская версия

### 📖 О проекте

Демонстрационный проект **полной автоматизации инфраструктуры** через **Ansible**:
от LEMP-стека до MongoDB replica set и Docker-контейнеров. Проект показывает
**Ansible-роли**, **Vault**, **мульти-ОС**, **Molecule** для тестирования ролей.

Проект создан в рамках курса **Slurm.io** (Ansible) + собственных экспериментов.

### 🛠 Технологии

| Компонент | Технология |
|---|---|
| **Автоматизация** | Ansible 2.21 (core) |
| **Роли** | nginx, mysql, php, python_app |
| **Секреты** | Ansible Vault (AES-256) |
| **Мульти-ОС** | Ubuntu 22.04/26.04 + CentOS Stream 9 |
| **Тестирование** | Molecule 26.10 + Docker driver |
| **Базы данных** | MySQL, PostgreSQL 18, MongoDB 7.0 |
| **Контейнеры** | Docker + community.docker |
| **Runtime** | Python 3.10/3.14 |

### 📋 Требования

- **Ansible** 2.20+ (core)
- **Python** 3.10+
- **Docker** (для Molecule и Docker-плейбуков)
- **Ubuntu 22.04+/CentOS Stream 9** (для мульти-ОС)
- **PostgreSQL 18**, **MongoDB 7.0**, **MySQL 8.0**

### 🚀 Как работает проект

1. **Inventory** — `inventory.ini` (localhost) + `inventory-ssh.ini` (SSH-хосты)
2. **Vault** — пароли в `group_vars/webservers/vault.yml` (AES-256)
3. **Роли** — `nginx`, `mysql`, `php`, `python_app`
4. **Playbook'и** — от простого `playbook-lemp.yml` до сложного `mongodb-replicaset-playbook.yml`
5. **Molecule** — тестирование роли `nginx` в Docker-контейнере
6. **Мульти-ОС** — ветвление `when: ansible_facts['os_family'] == 'Debian'/'RedHat'`

### 📁 Структура проекта


```
ansible-lemp/
├── ansible.cfg
├── inventory.ini
├── inventory-ssh.ini
├── requirements.yml
├── README.md
├── group_vars/
│   └── webservers/
│       ├── vars.yml
│       └── vault.yml
├── roles/
│   ├── nginx/
│   ├── mysql/
│   ├── php/
│   └── python_app/
├── playbook-lemp.yml
├── playbook-multi-os.yml
├── mongodb-replicaset-playbook.yml
├── docker-playbook.yml
├── docker-image-playbook.yml
└── docker-compose-playbook.yml
```

### 🎯 Быстрый старт

```bash
# 1. Клонировать репозиторий
git clone https://gitlab.com/vladimir_vgb/ansible-lemp.git
cd ansible-lemp

# 2. Установить роли и коллекции из Galaxy
ansible-galaxy install -r requirements.yml

# 3. Создать .vault_pass
echo "MyVaultPassword123!" > .vault_pass
chmod 600 .vault_pass

# 4. Проверить связь
ansible all -m ping

# 5. Развернуть LEMP
ansible-playbook playbook-lemp.yml
```

### 🔐 Ansible Vault

```bash
ansible-vault view group_vars/webservers/vault.yml
ansible-vault edit group_vars/webservers/vault.yml
ansible-vault rekey group_vars/webservers/vault.yml
```

### 🌍 Мульти-ОС (Ubuntu + CentOS)

```yaml
- name: Install nginx (Debian)
  apt:
    name: nginx
    state: present
  when: ansible_facts['os_family'] == 'Debian'

- name: Install nginx (RedHat)
  dnf:
    name: nginx
    state: present
  when: ansible_facts['os_family'] == 'RedHat'
```

### 🐘 PostgreSQL (Galaxy)

```bash
ansible-playbook postgres-playbook.yml
```

### 🍃 MongoDB replica set

```bash
ansible-playbook mongodb-replicaset-playbook.yml
```

### 🐳 Docker + Ansible

```bash
ansible-playbook docker-playbook.yml
ansible-playbook docker-image-playbook.yml
ansible-playbook docker-compose-playbook.yml
```

### 🧪 Molecule

```bash
cd roles/nginx
molecule test
```

### 🔧 Полезные команды

```bash
ansible-playbook playbook-lemp.yml --syntax-check
ansible-playbook playbook-lemp.yml --check --diff
ansible-playbook playbook-lemp.yml -vvv
cd roles/nginx && molecule test
```

### 🔗 Ссылки

- **GitLab**: https://gitlab.com/vladimir_vgb/ansible-lemp
- **Docker Hub**: https://hub.docker.com/u/zakon13

---

## 📄 License / Лицензия

MIT License / Лицензия MIT

