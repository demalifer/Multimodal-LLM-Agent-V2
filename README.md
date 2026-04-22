# Multimodal LLM Agent V2 (Day1)

## 项目目标
构建一个跨模态智能大模型助手，逐步支持：
- 文本、图片、表格输入
- 多轮问答与会话记忆
- 工具调用（Python / SQL / API）
- 参数高效微调（后续迭代）

> 当前为 Day1：完成后端工程化骨架，全部为 mock 实现，不接入真实模型。

## 目录结构

```text
.
├── app
│   ├── core
│   │   ├── input_router.py
│   │   ├── memory_manager.py
│   │   └── prompt_builder.py
│   ├── models
│   │   ├── fusion_module.py
│   │   ├── llm_loader.py
│   │   ├── table_encoder.py
│   │   └── vision_encoder.py
│   ├── router
│   │   └── chat.py
│   ├── schemas
│   │   ├── request.py
│   │   └── response.py
│   ├── service
│   │   └── chat_service.py
│   ├── tools
│   │   ├── api_executor.py
│   │   ├── python_executor.py
│   │   ├── sql_executor.py
│   │   └── tool_router.py
│   ├── utils
│   │   ├── file_loader.py
│   │   └── logger.py
│   └── main.py
└── requirements.txt
```

## 启动方式

### 1) 安装依赖
```bash
pip install -r requirements.txt
```

### 2) 启动服务
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 3) 调用接口
- Endpoint: `POST /chat`
- 请求示例：

```bash
curl -X POST 'http://127.0.0.1:8000/chat' \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "请帮我分析这张图并结合表格给结论",
    "session_id": "demo-session-1",
    "image_path": "./data/demo.png",
    "table_path": "./data/demo.csv"
  }'
```

- 返回示例（mock）：

```json
{
  "session_id": "demo-session-1",
  "answer": "[MOCK_LLM] ...",
  "used_modalities": ["text", "image", "table"],
  "tool_trace": "tool_router:none"
}
```

## Day1 已实现能力
- FastAPI 后端基础服务与路由
- `/chat` 接口定义与参数校验
- 模态输入路由、记忆管理、提示词构建
- 模型与工具层 mock 占位
- 工程化目录拆分，避免业务逻辑堆叠在 `main.py`

## 后续 Roadmap
- Day2: 接入真实模型推理链路（文本优先）
- Day3: 图片与表格真实编码器接入（多模态融合）
- Day4: 会话记忆升级（向量检索 + 摘要记忆）
- Day5: 工具调用协议标准化（函数调用 / ReAct）
- Day6: 评测与观测（日志、指标、trace）
- Day7: PEFT 训练流程设计（LoRA / QLoRA）
