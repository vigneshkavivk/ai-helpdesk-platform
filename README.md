Super 👍 Ippo **pods + services ellam running**. Next step → **application working aa nu test panna vendum**.

Since services are **ClusterIP** in Kubernetes, direct external access illa. So test panna **3 easy methods** irukku.

---

# 1️⃣ Method 1 — Port Forward (Easy)

AI service test panna:

```bash
kubectl port-forward svc/ai-service 5000:80
```

Ipdi run pannina terminal open ah vechikonga.

Then another terminal la run:

```bash
curl -X POST http://localhost:5000/analyze \
-H "Content-Type: application/json" \
-d '{"message":"vpn not working"}'
```

Expected output:

```json
{"intent":"network_issue"}
```

If idhu varudhu na **AI service working** ✅

---

# 2️⃣ Test Auth Service

Port forward:

```bash
kubectl port-forward svc/auth-service 5001:80
```

Test:

```bash
curl -X POST http://localhost:5001/login \
-H "Content-Type: application/json" \
-d '{"username":"admin","password":"password123"}'
```

Expected:

```json
{"status":"success"}
```

---

# 3️⃣ Test Ticket Service

Port forward:

```bash
kubectl port-forward svc/ticket-service 5002:80
```

Test create ticket:

```bash
curl -X POST http://localhost:5002/ticket \
-H "Content-Type: application/json" \
-d '{"message":"vpn not working"}'
```

Expected:

```json
{"id":1,"message":"vpn not working","status":"open"}
```

---

# 4️⃣ Test Notification Service

Port forward:

```bash
kubectl port-forward svc/notification-service 5003:80
```

Test:

```bash
curl -X POST http://localhost:5003/notify \
-H "Content-Type: application/json" \
-d '{"message":"ticket created"}'
```

Expected:

```json
{"status":"sent"}
```

---

# 5️⃣ Full Microservice Flow Test

Architecture:

```
User
 ↓
auth-service
 ↓
ai-service
 ↓
ticket-service
 ↓
notification-service
```

Each service test pannina **full system working** nu confirm pannalaam.

---

# 6️⃣ Extra Debug (If something fails)

Check logs:

```bash
kubectl logs <pod-name>
```

Example:

```bash
kubectl logs ai-service-66898cb48b-5ppq4
```

---

✅ If all curl commands work → **microservices platform successfully running** 🎉

---

If you want, next I can show **one powerful improvement**:

👉 **Expose entire AI Helpdesk system with one URL using Ingress + NGINX**

Example:

```
http://ai-helpdesk.local/ai
http://ai-helpdesk.local/login
```

Idhu **real production architecture** 🔥.
