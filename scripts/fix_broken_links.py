#!/usr/bin/env python3
"""Fix broken internal links across all content markdown files."""

import glob
import re

# Mapping: broken URL -> correct URL
LINK_MAP = {
    # Guides
    "/guides/what-is-model-context-protocol-mcp/": "/guides/what-is-mcp/",
    "/guides/mcp-server-directory/": "/guides/best-mcp-servers/",
    "/guides/mcp-security-best-practices/": "/guides/mcp-server-security/",
    "/contact/": "/about/",
    "/guides/building-mcp-servers/": "/guides/build-your-first-mcp-server/",
    "/guides/mcp-security/": "/guides/mcp-server-security/",
    "/guides/mcp-healthcare/": "/guides/mcp-healthcare-fhir/",
    "/guides/getting-started-with-mcp/": "/guides/what-is-mcp/",
    "/guides/how-mcp-works/": "/guides/what-is-mcp/",
    "/guides/mcp-and-apis/": "/guides/mcp-vs-rest-apis/",
    "/guides/mcp-error-handling-resilience-patterns/": "/guides/mcp-error-handling-resilience/",
    "/guides/mcp-enterprise-security/": "/guides/mcp-enterprise-infrastructure/",
    "/guides/mcp-database-servers/": "/guides/best-database-mcp-servers/",
    "/guides/mcp-iot-edge/": "/guides/mcp-iot-embedded-systems/",
    "/guides/mcp-kubernetes/": "/guides/best-kubernetes-container-mcp-servers/",
    "/guides/mcp-ci-cd/": "/guides/mcp-cicd-platform-integrations/",
    "/guides/mcp-python/": "/guides/mcp-server-frameworks-sdks/",
    "/guides/best-monitoring-mcp-servers/": "/guides/best-observability-mcp-servers/",
    "/guides/mcp-finance/": "/guides/mcp-finance-fintech/",
    "/guides/mcp-iot-smart-devices/": "/guides/mcp-iot-embedded-systems/",
    "/guides/mcp-cybersecurity/": "/guides/mcp-cybersecurity-threat-intelligence/",
    "/guides/mcp-iot/": "/guides/best-iot-mcp-servers/",
    "/guides/mcp-iot-hardware/": "/guides/mcp-iot-embedded-systems/",
    "/guides/mcp-financial-services/": "/guides/mcp-finance-fintech/",
    "/guides/collaboration-mcp-servers/": "/guides/mcp-real-time-collaboration/",

    # Reviews
    "/reviews/wearables-quantified-self-mcp-servers/": "/reviews/fitness-wearables-mcp-servers/",
    "/reviews/finance-mcp-servers/": "/reviews/personal-finance-mcp-servers/",
    "/reviews/cloud-platform-mcp-servers/": "/reviews/cloud-storage-mcp-servers/",
    "/reviews/content-copywriting-mcp-servers/": "/reviews/cms-content-management-mcp-servers/",
    "/reviews/design-ui-mcp-servers/": "/guides/best-design-mcp-servers/",
    "/reviews/devops-mcp-servers/": "/reviews/ci-cd-pipeline-mcp-servers/",
    "/reviews/scientific-research-mcp-servers/": "/reviews/science-research-mcp-servers/",
    "/reviews/data-science-ml-mcp-servers/": "/reviews/ai-ml-model-serving-mcp-servers/",
    "/reviews/iot-smart-home-mcp-servers/": "/reviews/smart-home-automation-mcp-servers/",
    "/reviews/cloud-infrastructure-mcp-servers/": "/reviews/infrastructure-as-code-mcp-servers/",
    "/reviews/email-communication-mcp-servers/": "/reviews/gmail-mcp-servers/",
    "/reviews/video-streaming-mcp-servers/": "/reviews/video-production-streaming-mcp-servers/",
    "/reviews/health-wellness-mcp-servers/": "/reviews/healthcare-medical-mcp-servers/",
    "/reviews/e-commerce-mcp-servers/": "/reviews/ecommerce-shopping-mcp-servers/",
    "/reviews/business-productivity-mcp-servers/": "/reviews/erp-business-management-mcp-servers/",
    "/reviews/design-creative-mcp-servers/": "/guides/best-design-mcp-servers/",
    "/reviews/code-quality-mcp-servers/": "/reviews/code-quality-linting-mcp-servers/",
    "/reviews/communication-messaging-mcp-servers/": "/reviews/telecommunications-messaging-mcp-servers/",
    "/reviews/web-scraping-mcp-servers/": "/reviews/web-scraping-crawling-mcp-servers/",
    "/reviews/ui-ux-design-mcp-servers/": "/guides/best-design-mcp-servers/",
    "/reviews/3d-printing-mcp-servers/": "/reviews/printing-3d-printing-mcp-servers/",
    "/reviews/weather-mcp-servers/": "/reviews/weather-climate-mcp-servers/",
    "/reviews/analytics-business-intelligence-mcp-servers/": "/reviews/analytics-mcp-servers/",
    "/reviews/maps-geolocation-mcp-servers/": "/reviews/geospatial-mapping-mcp-servers/",
    "/reviews/finance-trading-mcp-servers/": "/reviews/personal-finance-mcp-servers/",
    "/reviews/developer-tools-mcp-servers/": "/reviews/ide-code-editor-mcp-servers/",
    "/reviews/productivity-task-management-mcp-servers/": "/reviews/note-taking-knowledge-management-mcp-servers/",
    "/reviews/gmail-mcp-server/": "/reviews/gmail-mcp-servers/",
    "/reviews/security-mcp-servers/": "/reviews/security-scanning-mcp-servers/",
    "/reviews/database-mcp-servers/": "/reviews/database-admin-mcp-servers/",
    "/reviews/email-mcp-servers/": "/reviews/gmail-mcp-servers/",
    "/reviews/robotics-automation-mcp-servers/": "/reviews/robotics-mcp-servers/",
}

def fix_links():
    md_files = glob.glob("content/**/*.md", recursive=True)
    total_fixes = 0
    files_changed = 0

    for filepath in md_files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        original = content
        file_fixes = 0

        for broken, correct in LINK_MAP.items():
            # Match markdown links and Hugo relref patterns
            # Pattern 1: (broken_url) in markdown links
            old = f"]({broken})"
            new = f"]({correct})"
            count = content.count(old)
            if count > 0:
                content = content.replace(old, new)
                file_fixes += count

            # Pattern 2: without trailing slash
            broken_no_slash = broken.rstrip("/")
            correct_val = correct
            old2 = f"]({broken_no_slash})"
            new2 = f"]({correct_val})"
            count2 = content.count(old2)
            if count2 > 0:
                content = content.replace(old2, new2)
                file_fixes += count2

        if content != original:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            files_changed += 1
            total_fixes += file_fixes
            print(f"  Fixed {file_fixes} links in {filepath}")

    print(f"\nTotal: {total_fixes} links fixed across {files_changed} files")

if __name__ == "__main__":
    fix_links()
