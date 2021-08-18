from pathlib import Path
import os
import shutil


if __name__ == "__main__":
    basedir = Path().resolve()
    notebooksdir = basedir / "notebooks"
    outdir = basedir / "predictions"

    expts = [
        "efficientnetb0_100epoch",
        "efficientnetv2s_100epoch",
        "efficientnetv2s_640",
        "efficientnetb0_640",
        "tf_efficientnet_b1_ns"
    ]

    os.makedirs(outdir, exist_ok=True)

    for expt in expts:
        exptdir = notebooksdir / expt / "output"
        files = [f for f in os.listdir(exptdir) if ".csv" in f]

        os.makedirs(outdir / expt, exist_ok=True)
        for f in files:
            shutil.copy(exptdir / f, outdir / expt)
