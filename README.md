KubeCI - Automated CI/CD Deployment

A fully functional CI/CD pipeline that automates the containerization, testing, and deployment of a FastAPI application to a local Kubernetes cluster using Jenkins, GitHub Actions, Docker, Helm, and Minikube.

📌 Project Goals

  - Build a reproducible, local CI/CD setup that mimics real-world deployment practices.
  - Integrate Jenkins and GitHub Actions to create a GitOps-style delivery pipeline.
  - Use Docker and Kubernetes (Minikube) to run a FastAPI app in a containerized microservice.

🔧 Tech Stack

  - FastAPI – Lightweight Python web framework
  - Docker – For containerizing the application
  - Helm – To manage Kubernetes manifests and charts
  - Kubernetes (Minikube) – For local deployment and orchestration
  - Jenkins – Main CI/CD orchestrator
  - GitHub Actions – To trigger builds via webhooks
  - Ngrok – To expose Jenkins locally for webhook testing

🏗️ Project Architecture

  ![Architecture](https://github.com/user-attachments/assets/16a68a0b-6a1d-411d-8546-7312a4bafcfa)

✅ Architecture Validation:

   1. GitHub
    🔄 Used to store the FastAPI app and Helm chart.
    🔔 A webhook triggers a Jenkins job on every push.
    ✔️ Implemented using Git + webhook.

   2. Jenkins
    ⚙️ CI server that:
       - Pulls changes from GitHub.
       - Builds the Docker image.
       - Uses minikube as the Kubernetes backend.
         ✔️ I've done this using a Freestyle Jenkins job.

   3. Docker
    🐳 Builds container images for the FastAPI app.
    ✔️ I used Dockerfile + minikube image load.

   4. Minikube
    📦 The local Kubernetes cluster to deploy apps.
    ✔️ I deployed my app here using kubectl + helm.

   5. Helm
    📜 Template-based deployment using Helm charts.
    ✔️ I've created a working chart under k8s/helm-chart.

   6. Running FastAPI App
    🚀 The app runs on Minikube and is accessed via kubectl port-forward.
    ✔️ I verified this by accessing localhost:8000/docs.

🧩 Project Structure

  ├── app/                        # FastAPI application
  │   ├── main.py
  │   ├── modules.py
  │   └── routes.py
  ├── k8s/helm-chart/            # Helm chart for Kubernetes deployment
  │   ├── templates/
  │   └── values.yaml
  ├── Dockerfile
  ├── requirements.txt
  ├── Jenkinsfile (optional for scripted pipeline)
  └── README.md

🚀 How It Works

  - Code Commit: Push code to the GitHub repository.
  - Webhook Trigger: GitHub fires a webhook to Jenkins (via ngrok).
  - Jenkins Build: Jenkins pulls the code, builds the Docker image.
  - Helm Deploy: Jenkins deploys the image to Kubernetes using Helm.
  - Access App: Exposed on localhost:8000/docs via port-forward.

🧪 Testing the Setup

  # From the root of the repo
  docker build -t kubeci-fastapi-app .
  minikube start --driver=docker
  minikube image load kubeci-fastapi-app:latest
  cd k8s/helm-chart
  helm install kubeci ./kubeci
  kubectl get pods
  kubectl port-forward pod/<pod-name> 8000:8000
  # Visit http://localhost:8000/docs

💡 Key Highlights

  - Helm templates (values.yaml, deployment, service, liveness probes)
  - Port-forwarding FastAPI for local browsing
  - Webhook integration with ngrok and GitHub
  - Jenkins pipeline simulated using local agent

📈 Future Enhancements

  - Add Jenkinsfile for declarative pipeline
  - Automate image pushes to Docker Hub
  - Deploy to real cloud K8s (e.g., EKS, GKE)
  - Add unit testing and reports

## 📞 Credits

This project was built by Siva Ramakrishna Palaparthy as a CI/CD-enabled full-stack portfolio piece to demonstrate end-to-end application design and deployment.

M.S. Computer Science, Syracuse University  
Email: krishpalaparthy6768@gmail.com
