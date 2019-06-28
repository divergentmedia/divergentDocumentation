FROM        pandoc/latex:2.7.2

WORKDIR     /data

RUN tlmgr update --self && \
 tlmgr install sectsty && \
 tlmgr install titlesec && \
 tlmgr install adjustbox && \
 tlmgr install collectbox && \
 tlmgr install pdftex


# RUN     apt-get -yqq update && \
#         apt-get --no-install-recommends -yqq install blender && \
#         rm -rf /var/lib/apt/lists/*

# MAINTAINER  Colin McFadden <mcfa0086@umn.edu>

# ADD     stage.blend /opt/stage.blend

# CMD         ["--help"]
# ENTRYPOINT  ["blender"]
# ENV         LD_LIBRARY_PATH=/usr/local/lib
