servers=("server1" "server2" "server3")
for server in "${servers[@]}"; do
    configure_monitoring_agent "$server"
done

environments=("dev" "staging" "prod")
for env in "${environments[@]}"; do
    deploy_configuration "$env"
done

databases=("db1" "db2" "db3")
for db in "${databases[@]}"; do
    create_backup "$db"
done

log_files=("app.log" "access.log" "error.log")
for log_file in "${log_files[@]}"; do
    rotate_and_cleanup_logs "$log_file"
done

servers=("server1" "server2" "server3")
for server in "${servers[@]}"; do
    check_resource_utilization "$server"
done

servers=("server1" "server2" "server3")
for server in "${servers[@]}"; do
    check_resource_utilization "$server"
done
