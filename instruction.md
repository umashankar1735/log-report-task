Read the Apache-style access log located at /app/access.log.

Generate a JSON report and write it to /app/report.json.

Your report must satisfy all of the following:

1. Include a field named "total_requests" containing the total number of log entries.
2. Include a field named "unique_ips" containing the number of distinct client IP addresses found in the log.
3. Include a field named "top_path" containing the request path that appears most frequently in the log.
4. The output must be valid JSON written to /app/report.json.