from src import iter_dataset_paths
from src import pipeline_importer, model_importer
from src import dot_env_decorator
from src import randomised_order
from src import get_logger

logger = get_logger(__name__)


@dot_env_decorator
def main():
    pass
    # datasets = load_datasets_metadata()
    # pipelines = load_pipelines_metadata()
    # models = load_models_metadata()
    # for dataset_name in randomised_order(iter_dataset_paths()):
    #     for pipeline_name in randomised_order(pipelines.keys()):
    #         pipeline = pipeline_importer(pipeline_name, name=dataset_name)
    #         for model_name in randomised_order(models.keys()):
    #             logger.info(f"dataset={dataset_name} pipeline={pipeline_name} model={model_name}")
    #             model_importer(model_name, parent=pipeline).evaluate_outputs()


if __name__ == "__main__":
    main()
