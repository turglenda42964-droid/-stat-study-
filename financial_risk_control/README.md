# Financial Risk Control

工业级金融风控系统 Python 项目脚手架。

## 目录说明

- `config/`: 应用与数据库配置
- `data/`: 数据接入、处理、Schema
- `features/`: 特征工程与选择
- `models/`: 机器学习/深度学习模型、训练与评估
- `decision_engine/`: 规则和策略决策
- `serving/`: API 与实时决策服务
- `monitoring/`: 指标、告警、看板配置
- `deployment/`: Docker/K8s 部署文件
- `tests/`: 单测、集成、性能测试

## 快速开始

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
pytest -q
uvicorn financial_risk_control.serving.api.app:app --reload
```
