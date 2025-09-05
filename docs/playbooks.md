
ansible-playbook playbooks/{playbook}.yaml \                                                                                                                         
  -i {inventory} \                                                                                                                                              
  --extra-vars "ansible_user=admin ansible_password=secret"
