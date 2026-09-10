/* =========================================================
   RUANG USAHA
   SCRIPT.JS
   ========================================================= */


/* =========================================================
   1. MENU MOBILE
   ========================================================= */

const menuToggle = document.getElementById("menuToggle");
const nav = document.querySelector(".nav");

if (menuToggle && nav) {

    menuToggle.addEventListener("click", () => {

        nav.classList.toggle("active");

        const isOpen = nav.classList.contains("active");

        menuToggle.setAttribute(
            "aria-expanded",
            isOpen
        );

        menuToggle.textContent =
            isOpen ? "✕" : "☰";

    });

}


/* =========================================================
   2. TUTUP MENU SAAT LINK DIKLIK
   ========================================================= */

document.querySelectorAll(".nav a").forEach((link) => {

    link.addEventListener("click", () => {

        if (nav) {
            nav.classList.remove("active");
        }

        if (menuToggle) {

            menuToggle.textContent = "☰";

            menuToggle.setAttribute(
                "aria-expanded",
                "false"
            );

        }

    });

});


/* =========================================================
   3. MODAL LOGIN
   ========================================================= */

const loginBtn =
    document.getElementById("loginBtn");

const loginModal =
    document.getElementById("loginModal");


/* =========================================================
   4. MODAL REGISTER
   ========================================================= */

const registerBtn =
    document.getElementById("registerBtn");

const startBtn =
    document.getElementById("startBtn");

const registerModal =
    document.getElementById("registerModal");


/* =========================================================
   5. CURHAT USAHA
   ========================================================= */

const curhatBtn =
    document.getElementById("curhatBtn");


/* =========================================================
   6. FUNGSI MEMBUKA MODAL
   ========================================================= */

function openModal(modal) {

    if (!modal) return;

    modal.classList.add("active");

    document.body.style.overflow = "hidden";

}


/* =========================================================
   7. FUNGSI MENUTUP MODAL
   ========================================================= */

function closeModal(modal) {

    if (!modal) return;

    modal.classList.remove("active");

    document.body.style.overflow = "";

}


/* =========================================================
   8. LOGIN
   ========================================================= */

if (loginBtn) {

    loginBtn.addEventListener("click", () => {

        openModal(loginModal);

    });

}


/* =========================================================
   9. DAFTAR SEKARANG
   ========================================================= */

if (registerBtn) {

    registerBtn.addEventListener("click", () => {

        openModal(registerModal);

    });

}


/* Tombol Mulai Belajar */

if (startBtn) {

    startBtn.addEventListener("click", () => {

        openModal(registerModal);

    });

}


/* =========================================================
   10. CURHAT USAHA
   ========================================================= */

if (curhatBtn) {

    curhatBtn.addEventListener("click", () => {

        openModal(registerModal);

    });

}


/* =========================================================
   11. TOMBOL CLOSE SEMUA MODAL
   ========================================================= */

document.querySelectorAll("[data-close]")
    .forEach((button) => {

        button.addEventListener("click", () => {

            closeModal(loginModal);

            closeModal(registerModal);

        });

    });


/* =========================================================
   12. KLIK AREA LUAR MODAL
   ========================================================= */

[loginModal, registerModal]
    .forEach((modal) => {

        if (!modal) return;

        modal.addEventListener("click", (event) => {

            if (event.target === modal) {

                closeModal(modal);

            }

        });

    });


/* =========================================================
   13. TOMBOL ESC
   ========================================================= */

document.addEventListener("keydown", (event) => {

    if (event.key !== "Escape") return;

    closeModal(loginModal);

    closeModal(registerModal);

});


/* =========================================================
   14. PINDAH LOGIN → REGISTER
   ========================================================= */

const registerFromLogin =
    document.getElementById(
        "registerFromLogin"
    );

if (registerFromLogin) {

    registerFromLogin.addEventListener(
        "click",
        () => {

            closeModal(loginModal);

            openModal(registerModal);

        }
    );

}


/* =========================================================
   15. LOGIN FORM
   ========================================================= */

const loginForm =
    document.getElementById("loginForm");

if (loginForm) {

    loginForm.addEventListener(
        "submit",
        (event) => {

            event.preventDefault();

            showToast(
                "Login berhasil! Selamat datang di Ruang Usaha."
            );

            closeModal(loginModal);

            loginForm.reset();

        }
    );

}


/* =========================================================
   16. REGISTER FORM
   ========================================================= */

const registerForm =
    document.getElementById(
        "registerForm"
    );

if (registerForm) {

    registerForm.addEventListener(
        "submit",
        (event) => {

            event.preventDefault();

            showToast(
                "Pendaftaran berhasil! Selamat bergabung di Ruang Usaha."
            );

            closeModal(registerModal);

            registerForm.reset();

        }
    );

}


/* =========================================================
   17. TOAST NOTIFICATION
   ========================================================= */

const toast =
    document.getElementById("toast");

const toastMessage =
    document.getElementById(
        "toastMessage"
    );

let toastTimer;


function showToast(message) {

    if (!toast) return;

    if (toastMessage) {

        toastMessage.textContent =
            message;

    }

    toast.classList.add("show");

    clearTimeout(toastTimer);

    toastTimer = setTimeout(() => {

        toast.classList.remove("show");

    }, 3500);

}


/* =========================================================
   18. SERVICE CARD
   ========================================================= */

const serviceButtons =
    document.querySelectorAll(
        ".service-link"
    );

serviceButtons.forEach((button) => {

    button.addEventListener(
        "click",
        () => {

            const service =
                button.dataset.service ||
                "Layanan Ruang Usaha";

            showToast(
                `${service} akan segera tersedia di aplikasi.`
            );

        }
    );

});


/* =========================================================
   19. DIGITAL BUTTON
   ========================================================= */

const digitalButtons =
    document.querySelectorAll(
        ".digital-buttons button"
    );

digitalButtons.forEach((button) => {

    button.addEventListener(
        "click",
        () => {

            showToast(
                "Fitur digital Ruang Usaha akan terhubung pada tahap berikutnya."
            );

        }
    );

});


/* =========================================================
   20. SMOOTH SCROLL
   ========================================================= */

document.querySelectorAll(
    'a[href^="#"]'
).forEach((link) => {

    link.addEventListener(
        "click",
        (event) => {

            const targetId =
                link.getAttribute("href");

            if (
                !targetId ||
                targetId === "#"
            ) {
                return;
            }

            const target =
                document.querySelector(
                    targetId
                );

            if (!target) return;

            event.preventDefault();

            target.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });

        }
    );

});


/* =========================================================
   21. TAHUN FOOTER OTOMATIS
   ========================================================= */

const yearElement =
    document.getElementById("year");

if (yearElement) {

    yearElement.textContent =
        new Date().getFullYear();

}


/* =========================================================
   22. ANIMASI SAAT SCROLL
   ========================================================= */

const animatedElements =
    document.querySelectorAll(
        ".service-card, .feature-card, .timeline-item, .target-item"
    );


if (
    "IntersectionObserver" in window &&
    animatedElements.length > 0
) {

    const observer =
        new IntersectionObserver(
            (entries) => {

                entries.forEach(
                    (entry) => {

                        if (
                            entry.isIntersecting
                        ) {

                            entry.target.style.opacity =
                                "1";

                            entry.target.style.transform =
                                "translateY(0)";

                            observer.unobserve(
                                entry.target
                            );

                        }

                    }
                );

            },
            {
                threshold: 0.12
            }
        );


    animatedElements.forEach(
        (element) => {

            element.style.opacity = "0";

            element.style.transform =
                "translateY(20px)";

            element.style.transition =
                "opacity 0.6s ease, transform 0.6s ease";

            observer.observe(element);

        }
    );

}


/* =========================================================
   23. PREVENT MODAL FORM ENTER PROBLEM
   ========================================================= */

document.querySelectorAll(
    ".modal input"
).forEach((input) => {

    input.addEventListener(
        "keydown",
        (event) => {

            if (
                event.key === "Escape"
            ) {

                closeModal(loginModal);

                closeModal(registerModal);

            }

        }
    );

});


/* =========================================================
   24. CONSOLE
   ========================================================= */

console.log(
    "Ruang Usaha berhasil dijalankan."
);

console.log(
    "Belajar • Berbagi • Bertumbuh Bersama"
);