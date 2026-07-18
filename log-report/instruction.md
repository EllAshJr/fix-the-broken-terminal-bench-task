Analyze the Apache-style access log at `/app/access.log` and write the requested summary to `/app/report.json`. Treat each non-empty line as one request record. The output must be a UTF-8 JSON object; do not rename the file or write the result elsewhere.

1. `/app/report.json` exists, parses as a JSON object, and contains exactly three keys: `total_requests`, `unique_ips`, and `top_path`. `total_requests` and `unique_ips` are integers, and `top_path` is a string.
2. `total_requests` equals the number of non-empty request records in `/app/access.log`.
3. `unique_ips` equals the number of distinct client IP addresses, where the client IP is the first whitespace-delimited field of each record.
4. `top_path` equals the most frequently requested request-target, where the request-target is the second whitespace-delimited token inside the quoted HTTP request field.
