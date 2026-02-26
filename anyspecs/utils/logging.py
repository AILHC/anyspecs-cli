"""
Logging configuration and utilities.
"""

import logging
import sys
import io
from typing import Optional


# 强制使用 UTF-8 编码输出（兼容 Windows）
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')


def setup_logging(level: Optional[str] = None, verbose: bool = False) -> logging.Logger:
    """
    Set up logging configuration.

    Args:
        level: Log level as string (DEBUG, INFO, WARNING, ERROR)
        verbose: Enable verbose logging (sets to DEBUG)

    Returns:
        Configured logger instance
    """
    if verbose:
        log_level = logging.DEBUG
    elif level:
        log_level = getattr(logging, level.upper(), logging.INFO)
    else:
        log_level = logging.INFO

    # 配置输出流使用 UTF-8
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(log_level)

    # Configure root logger
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[stdout_handler],
        force=True  # 确保重新配置
    )
    
    # Return logger for the package
    logger = logging.getLogger('anyspecs')
    return logger


def get_logger(name: str) -> logging.Logger:
    """Get a logger for a specific module."""
    return logging.getLogger(f'anyspecs.{name}') 