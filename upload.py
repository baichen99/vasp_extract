from template_tools.src.upload import upload_job

upload_job('zip', '第一性原理计算数据', '第一性原理计算数据(vasp)', file_paths=['outputs'], max_workers=1)