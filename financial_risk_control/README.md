# Financial Risk Control

工业级金融风控系统 Python 项目模板（可直接二次开发）。

## 核心能力

- 分层架构：配置、数据、特征、模型、决策、服务、监控、部署。
- FastAPI 在线评分接口，内置认证中间件与请求日志中间件。
- 决策工作流支持规则前置拦截 + 策略执行（PASS/REVIEW/BLOCK）。
- 支持环境变量配置、容器化部署、基础单测与工程命令。

## 目录说明

- `config/`: 应用配置与数据库配置
- `data/`: 数据连接器、处理器、Schema
- `features/`: 特征计算、筛选、流水线
- `models/`: 模型抽象、ML/DL、训练与评估
- `decision_engine/`: 规则引擎、策略管理、工作流
- `serving/`: API 服务与实时决策
- `monitoring/`: 模型/系统指标与告警
- `deployment/`: Docker 与 K8s 配置
- `tests/`: 单元/集成/性能测试

## 快速开始

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
cp .env.example .env
pytest -q
uvicorn financial_risk_control.serving.api.app:app --reload
```

## API 示例

```bash
curl -X POST 'http://127.0.0.1:8000/api/v1/risk/score' \
  -H 'Content-Type: application/json' \
  -H 'X-API-Token: dev-token' \
  -d '{"customer_id":"C001","amount":50000,"night_ratio":0.6}'
```
