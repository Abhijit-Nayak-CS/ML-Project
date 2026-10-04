## End to End Machine Learning Project

Run the training pipeline from the repository root so Python can resolve the
`src` package:

```powershell
python -m src.components.data_ingestion
```

In VS Code, use **Run and Debug** and select **Train model**. Do not run
`src/components/data_ingestion.py` directly; direct-file execution does not put
the repository root on Python's import path.

