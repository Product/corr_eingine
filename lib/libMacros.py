macros = {"$IP":r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
          "$PORT":r"[\d]{1,5}",
          "$SCISCOTIMEHOST":r"^<[\d]+>(?P<date>[^ ]+\s[^ ]+\s[^ ]+\s[\d]+:[\d]+:[\d]+)\s(?P<h_name>[^ ]+)\s:\s+%ASA-(?P<v_id>\d-\d{1,8}):",
          "$SSPT":r"(?P<spt>[\d]{1,5})",
          "$SDPT":r"(?P<dpt>[\d]{1,5})",
          "$SSRC":r"(?P<ips>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",
          "$SDST":r"(?P<ipd>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",
          "$SFADDR":r"(?P<faddr>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",
          "$SLADDR":r"(?P<laddr>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",
          "$SGADDR":r"(?P<gaddr>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"}