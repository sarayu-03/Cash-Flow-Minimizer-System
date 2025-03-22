import os
import subprocess
import logging
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import default_storage

logger = logging.getLogger(__name__)


def home(request):
    return render(request, "example/home.html", {})

import os
import subprocess
import logging
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.core.files.storage import default_storage

logger = logging.getLogger(__name__)


def home(request):
    return render(request, "example/home.html", {})


def visualize(request):
    if request.method == "POST":
        banks_file = request.FILES.get("banksFile")
        transactions_file = request.FILES.get("transactionsFile")

        if banks_file and transactions_file:
            try:
                # Save the uploaded files temporarily
                banks_file_path = default_storage.save(banks_file.name, banks_file)
                transactions_file_path = default_storage.save(
                    transactions_file.name, transactions_file
                )

                banks_file_absolute_path = default_storage.path(banks_file_path)
                transactions_file_absolute_path = default_storage.path(
                    transactions_file_path
                )

                logger.debug(f"Saved banks file: {banks_file_absolute_path}")
                logger.debug(
                    f"Saved transactions file: {transactions_file_absolute_path}"
                )

                # Set the path to the C++ executable
                exe_path = os.path.join(
                    settings.BASE_DIR, "static", "run.sh"
                )
                os.chmod(exe_path, 0o755)

                # Run the C++ program with the two file paths as arguments
                result = subprocess.run(
                    [
                        exe_path,
                        banks_file_absolute_path,
                        transactions_file_absolute_path,
                    ],
                    capture_output=True,
                    text=True,
                    shell=False,
                )

                # Check if the C++ program ran successfully
                if result.returncode == 0:
                    output = result.stdout
                else:
                    output = result.stderr
                    logger.error(f"Program error: {output}")

                # Clean up the saved files after processing
                default_storage.delete(banks_file_path)
                default_storage.delete(transactions_file_path)

                return JsonResponse({"answer": output})

            except Exception as e:
                logger.error(f"Error processing files: {e}")
                return JsonResponse({"error": "Internal server error"}, status=500)

        else:
            return JsonResponse(
                {"error": "Both banks file and transactions file are required"},
                status=400,
            )

    return render(request, "example/home.html")


def favicon(request):
    return HttpResponse(status=204)
