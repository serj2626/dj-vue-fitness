def get_path_for_avatar_for_trainer(instance, filename):
    return f"trainers/{instance.position}/{instance.first_name}{instance.last_name}/{filename}"


def get_path_for_all_images_by_trainer(instance, filename):
    return f"trainers/{instance.trainer.position}/{instance.trainer.first_name}{instance.trainer.last_name}/gallery/{filename}"
