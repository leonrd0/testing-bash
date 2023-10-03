cfg = rs.conf()
cfg.members[0].host = "@HOSTNAME@"
rs.reconfig(cfg)