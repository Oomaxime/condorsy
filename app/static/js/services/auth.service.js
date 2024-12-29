const AuthService = {
  async login(pseudo, password) {
    try {
      const response = await fetch("/api/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Cache-Control": "no-cache", // Désactiver le cache
        },
        body: JSON.stringify({pseudo, password}),
      });

      if (!response.ok) {
        throw new Error("Échec de la connexion");
      }

      const data = await response.json();
      if (data.token) {
        localStorage.setItem("token", data.token);
        localStorage.setItem("user", JSON.stringify(data.user));
      }
      return data;
    } catch (error) {
      console.error("Erreur lors de la connexion:", error);
      throw error;
    }
  },

  logout() {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    window.location.href = "/";
  },

  getCurrentUser() {
    const token = this.getToken();
    if (!token) return null;

    // Décode le payload du token (partie entre les deux points)
    const payload = JSON.parse(atob(token.split(".")[1]));
    return {
      pseudo: payload.pseudo,
      date_of_birth: payload.date_of_birth,
      addresse: payload.addresse,
      job: payload.job,
      admin: payload.admin,
    };
  },

  getToken() {
    return localStorage.getItem("token");
  },

  isAuthenticated() {
    return !!this.getToken();
  },
};
