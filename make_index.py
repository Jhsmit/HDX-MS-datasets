# %%

from hdxms_datasets import DataVault
from pathlib import Path
import pandas as pd

# %%


def make_index(vault: DataVault) -> pd.DataFrame:
    records = []
    for datset_id in vault.datasets:
        try:
            record = {"dataset_id": datset_id}
            metadata = vault.get_metadata(datset_id)
            record["name"] = metadata["protein"]["name"]
            record["uniprot_id"] = metadata["protein"]["uniprot_id"]
            records.append(record)
        except KeyError:
            pass

    return pd.DataFrame(records)


# %%

dataset_dir = Path("./datasets")
vault = DataVault(dataset_dir)

index_df = make_index(vault)
index_df.to_csv(dataset_dir / "index.csv")

# %%
