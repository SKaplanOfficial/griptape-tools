# GPT Scripter

A collection of custom [Griptape](https://github.com/griptape-ai/griptape) tools for intelligently automating macOS using AppleScript.

## Documentation

### AppleScriptRunner

Completes tasks by generating and executing AppleScript code.

```python
from decouple import config
from griptape.flow.memory import PipelineMemory
from griptape.flow.steps import PromptStep, ToolkitStep
from griptape.flow.structures import Pipeline
from griptape.flow.utils import ToolLoader
from griptape.flow.drivers import OpenAiPromptDriver
from gptscripter.tools import AppleScriptRunner

AppleScripter = AppleScriptRunner()

pipeline = Pipeline(
    memory=PipelineMemory(),
    prompt_driver=OpenAiPromptDriver(
        model="gpt-3.5-turbo",
        api_key=config("OPENAI_API_KEY")
    ),
    tool_loader=ToolLoader(
        tools=[AppleScripter]
    )
)

pipeline.add_steps(
    ToolkitStep(
        tool_names=[AppleScripter.name]
    ),
    PromptStep(
        "Summarize this: {{ input }}"
    )
)

pipeline.run("Play Don't Stop Believin'.")
print(pipeline.memory.runs[-1].output)
```

## License

These tools are available under the Apache 2.0 License.
