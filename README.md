# Distributed Systems Group Project

## Group 1: Load balancer to MPI based service

### Group Members

| No | Student ID | Name            | GitHub id | Role |
|----|------------|-----------------|-----------|------|
| 1  | BI12-243 | Le Vu Hoang Linh | r4m0D | Team Leader, Developer - Trapezoidal Algorithm Implementation |
| 2  | BI12-416 | Do Nhat Thanh | f1sh33 | Consultant, Presentation Specialist |
| 3  | BI12-467 | Tran Duc Tuan | cs8u7 | Developer - Load Balancer Implementation |
| 4  | BI12-368 | Vu Ngoc Minh Quan | vnkunnq | Developer - Docker Configuration |
| 5  | BI12-325 | Nguyen Duc Nguyen | ducnguyen2410 | Report Writer - Theoretical Foundations |
| 6  | BI12-468 | Tran Nguyen Kien Tuan | Tuso-shadoq | Report Writer - Project Documentation |

## Theoretical Foundations

## Implementation Details

## Build and Deployment Guide

**Dependencies:** Docker, Docker Compose

**Steps*:**
1. Clone the repository
2. Run the following command to build the docker images and start the services:
```bash
docker-compose up --build
```
**Note:** If you encounter the error `failed to solve: python:3.8-slim: error getting credentials - err: exit status 1, out: \`\` `, try manually pulling the base image with docker pull python:3.8-slim.



