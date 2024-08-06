def get_path_for_avatar_for_trainer(instance, filename):
    return f"trainers/{instance.position}/{instance.first_name}{instance.last_name}/{filename}"
